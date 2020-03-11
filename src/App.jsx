/*
Kaptos UI  App
*/

import React, { useState, useEffect } from "react";
import { useAsync } from "react-async";

// React BootStrap
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import Form from "react-bootstrap/Form";
import FormControl from "react-bootstrap/FormControl";
import Button from "react-bootstrap/Button";
import "bootstrap/dist/css/bootstrap.min.css";

// Installed
import Popup from "reactjs-popup";
import DayPicker, { DateUtils } from "react-day-picker";
import "react-day-picker/lib/style.css";

// Kaptos UI
import Map from "./Map/Map";
import Marker from "./Map/Marker";
import HeatmapLayer from "./Map/HeatmapLayer";
import "./App.css";

// Unix timestamp converter
function timeConverter(timestamp) {
  var a = new Date(timestamp * 1000);
  var months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
  ];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
  var time =
    date + " " + month + " " + year + " " + hour + ":" + min + ":" + sec;
  return time;
}

// Load reports example data
const loadReports = async () =>
  await fetch("./reports.json")
    .then(res => (res.ok ? res : Promise.reject(res)))
    .then(res => res.json());

// App
export default function App() {
  // VARs
  const defaults = {
    center: {
      lat: 49.207917,
      lng: -122.9736016
    },
    zoom: 11
  };

  // Raw report data states
  const [reportData, setReportData] = useState([]);
  const [totalReports, setTotalReports] = useState(0);

  // Manipulated data states
  const [filteredReports, setFilteredReports] = useState([]);
  const [selectedReport, setSelectedReport] = useState(0);
  const [reportIndex, setReportIndex] = useState(0);

  // Map states
  const [bounds, setBounds] = useState({});
  const [center, setCenter] = useState(defaults.center);
  const [heatmapLayerEnabled, setHeatmapLayerEnabled] = useState(false);

  // Calendar states
  const [dateFrom, setDateFrom] = useState();
  const [dateTo, setDateTo] = useState();
  const [dateRange, setDateRange] = useState();

  // Data states
  const [isLoaded, setIsLoaded] = useState(false);

  // Build reports list based on visible bounds
  useEffect(() => {
    setFilteredReports(filterByBounds());
  }, [bounds]);

  // Styles
  const ListItemStyles = {
    true: {
      borderRight: "5px solid red"
    },
    false: {
      bordeRight: "0px solid red"
    }
  };

  // List item element
  const ListItem = ({
    id,
    index,
    name,
    active,
    lat,
    lng,
    frequency,
    interference,
    strength,
    time,
    callsign
  }) => (
    <div
      id={"reportListItem" + id}
      className={["listItem", "strength" + strength].join(" ")}
      style={ListItemStyles[active]}
      onClick={() => {
        setReportIndex(index);
        setSelectedReport(id);
      }}
    >
      Report ID: {id} <br />
      Frequency: {frequency} <br />
      Interference: {interference}
      <br />
      Strength: {strength}
      <br />
      Time: {time}
      <br />
      Reported by: {callsign}
    </div>
  );

  // Marker elements
  let Markers = filteredReports.map((marker, index) => {
    return (
      <Marker
        key={"MID" + marker.id}
        index={index}
        active={marker.id == selectedReport}
        title={"Report ID: " + marker.id}
        position={{ lat: marker.lat, lng: marker.lng }}
        events={{
          onClick: () => {
            setCenter({ lat: marker.lat, lng: marker.lng });
            setSelectedReport(marker.id);
            setReportIndex(index);
            let targetReportListItem = document.getElementById(
              "reportListItem" + marker.id
            );
            targetReportListItem.scrollIntoView({
              behavior: "smooth",
              block: "end",
              inline: "nearest"
            });
          }
        }}
      />
    );
  });

  // List element
  let ReportsList = filteredReports.map((report, index) => {
    return (
      <ListItem
        key={report.id}
        index={index}
        name={report.id}
        id={report.id}
        active={report.id == selectedReport}
        lat={report.lat}
        lng={report.lng}
        frequency={report.frequency}
        interference={report.interference}
        frequency={report.frequency}
        strength={report.strength}
        time={timeConverter(report.time)}
        callsign={report.callsign}
      />
    );
  });

  // Filter reports based on makers visible in map bounds
  function filterByBounds() {
    let visibleMarkers = [];
    for (let report in reportData) {
      if (
        bounds.contains({
          lat: reportData[report].lat,
          lng: reportData[report].lng
        })
      ) {
        visibleMarkers.push(reportData[report]);
      }
    }
    return visibleMarkers;
  }

  function dateHandleDayClick(day) {
    const range = DateUtils.addDayToRange(day, { from: dateFrom, to: dateTo });
    setDateFrom(range.from);
    setDateTo(range.to);
  }

  function dateHandleResetClick() {
    setDateFrom(null);
    setDateTo(null);
  }

  // Async data load
  const { data, error, isLoading, isResolved } = useAsync({
    promiseFn: loadReports
  });

  if (isLoading && !isLoaded) {
    return <div>Loading...</div>;
  }

  if (error && !isLoaded) {
    return <div>Error...</div>;
  }

  if (data && isResolved && !isLoaded) {
    setReportData(data);
    setTotalReports(data.length);
    setFilteredReports(data);
    setReportIndex(0);
    setIsLoaded(true);
    return <div>Staging data...</div>;
  }

  if (isLoaded) {
    // Render interface
    return (
      <Container fluid="true" style={{ height: "100%", padding: "0px" }}>
        <Row noGutters="true" style={{ height: "8%" }}>
          <Navbar bg="light" expand="lg" style={{ width: "100%" }}>
            <Navbar.Brand href="#home">Kaptos</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="mr-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#link">About</Nav.Link>
                <NavDropdown title="Reports" id="basic-nav-dropdown">
                  <NavDropdown.Item href="#action/3.1">
                    Last 7 days
                  </NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.2">
                    Last 2 Weeks
                  </NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.3">
                    Last Month
                  </NavDropdown.Item>
                  <NavDropdown.Divider />
                  <NavDropdown.Item href="#action/3.4">
                    Year to date
                  </NavDropdown.Item>
                </NavDropdown>
              </Nav>

              <Form inline>
                <FormControl
                  type="text"
                  placeholder="Search"
                  className="mr-sm-2"
                />
                <Button variant="outline-success">Search</Button>
              </Form>
            </Navbar.Collapse>
          </Navbar>
        </Row>

        <Row style={{ height: "92%" }} noGutters="true">
          <Col xs={6} md={4} id="leftColumn">
            <div id="controlsContainer">
              <div style={{}} id="filterContainer">
                <h3>Filters</h3>
                <Popup
                  trigger={<Button className="btn">Date Range Filter</Button>}
                  position="right top"
                  contentStyle={{ width: "300px" }}
                >
                  <p>
                    {!dateFrom && !dateTo && "Please select the first day."}
                    {dateFrom && !dateTo && "Please select the last day."}
                    {dateFrom &&
                      dateTo &&
                      `Selected from ${dateFrom.toLocaleDateString()} to
                ${dateTo.toLocaleDateString()}`}{" "}
                    {dateFrom && dateTo && (
                      <Button className="btn" onClick={dateHandleResetClick}>
                        Reset
                      </Button>
                    )}
                  </p>
                  <DayPicker
                    className="Selectable"
                    numberOfMonths={1}
                    selectedDays={[dateFrom, { dateFrom, dateTo }]}
                    modifiers={{ start: dateFrom, end: dateTo }}
                    onDayClick={dateHandleDayClick}
                  />
                </Popup>
                <Button className="btn" disabled={true}>
                  Callsign Filter
                </Button>
                <Button className="btn" disabled={true}>
                  Strength Filter
                </Button>
              </div>
              <hr/>
              <div style={{}} id="infoContainer">
                Report ID: {selectedReport}. {filteredReports.length} of{" "}
                {totalReports} visible.
              </div>
              <div style={{}} id="controlContainer">
                <Button
                  className="btn"
                  onClick={() => {
                    let newReportIndex = 0;
                    newReportIndex =
                      (newReportIndex +
                        (reportIndex - 1) +
                        filteredReports.length) %
                      filteredReports.length; // Add filteredReports.length to newReportIndex and reportIndex less one to keep the result positive
                    setSelectedReport(filteredReports[newReportIndex].id);
                    setReportIndex(newReportIndex);
                  }}
                >
                  Previous Report
                </Button>
                <Button
                  className="btn"
                  onClick={() => {
                    let newReportIndex =
                      (reportIndex + 1) % filteredReports.length;
                    setSelectedReport(filteredReports[newReportIndex].id);
                    setReportIndex(newReportIndex);
                  }}
                >
                  Next Report
                </Button>
                <Button
                  className="btn"
                  disabled={true}
                  onClick={() => {
                    // TODO: Generate heatmap layer based on strength values
                    setHeatmapLayerEnabled(!heatmapLayerEnabled);
                  }}
                >
                  Toggle interference heatmap layer
                </Button>
              </div>
            </div>

            <div id="listContainer">{ReportsList}</div>
          </Col>

          <Col xs={12} md={8} id="mapContainer" style={{ height: "100%" }}>
            <Map
              zoom={defaults.zoom}
              center={center}
              events={{ onBoundsChanged: arg => setBounds(arg) }}
            >
              {Markers}
              <HeatmapLayer enabled={heatmapLayerEnabled} />
            </Map>
          </Col>
        </Row>
      </Container>
    );
  }
}
