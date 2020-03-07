/*
Kaptos UI  App
*/

import React, { useState, useEffect } from "react";
import { useAsync, IfPending, IfFulfilled, IfRejected } from "react-async"
import { Link, DirectLink, Element , Events, animateScroll, scrollSpy, scroller } from 'react-scroll'

// React BootStrap
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';

// Kaptos UI
import Map from "./Map/Map";
import Marker from "./Map/Marker";
import HeatmapLayer from "./Map/HeatmapLayer";
import './App.css';

// Unix timestamp converter
function timeConverter(timestamp){
  var a = new Date(timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes();
  var sec = a.getSeconds();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
  return time;
}

// Load reports data
const loadReports = async () =>
  await fetch("./reports.json")
    .then(res => (res.ok ? res : Promise.reject(res)))
    .then(res => res.json())

export default function App() {

  const defaults = {
    center: {
      lat: 49.207917,
      lng: -122.9736016
    },
    zoom: 11
  };

  const [ reportData, setReportData ] = useState([]);
  const [ filteredReports, setFilteredReports ] = useState([]);
  const [ reportIndex, setReportIndex ] = useState(0);
  const [ bounds, setBounds ] = useState({});
  const [ center, setCenter ] = useState(defaults.center);
  const [ heatmapLayerEnabled, setHeatmapLayerEnabled ] = useState(false);
  const [ isLoaded, setIsLoaded ] = useState(false);

  useEffect(() => {
    setFilteredReports(filterByBounds());
  }, [bounds]);

  const ListItemStyles = {
    'true': {
      'borderRight': '3px solid red'
    },
    'false': {
      'bordeRight': '0px solid red'
    }
  }

  const ListItem = ({
    id,
    name,
    active,
    lat,
    lng,
    frequency,
    interference,
    strength,
    time,
    callsign
  }) => <div id={'reportList' + id} className={['listItem', 'strength'+strength].join(' ')} style={ListItemStyles[active]}>Frequency: {frequency} <br />Interference: {interference}<br />Strength:{strength}<br/>Time: {time}<br/>Repoted by: {callsign}</div>;

  function filterByBounds() {
    let visibleMarkers = [];
    for (let report in reportData) {
      if (bounds.contains({ lat: reportData[report].lat, lng: reportData[report].lng })) {
        visibleMarkers.push(reportData[report]);
      }
    }
    return visibleMarkers;
  }

  function scrollTo(element, offset=0) {
    scroller.scrollTo(element, {
      duration: 300,
      delay: 0,
      smooth: 'easeInOutQuart',
      offset: offset
    })
  }

  function scrollToWithContainer(container, element) {
      console.log("Scrolling to:" + element);

    let goToContainer = new Promise((resolve, reject) => {

      Events.scrollEvent.register('end', () => {
        resolve();
        Events.scrollEvent.remove('end');
      });
/*
      scroller.scrollTo(container, {
        duration: 500,
        delay: 0,
        smooth: 'easeInOutQuart'
      });
*/
    });

    goToContainer.then(() =>
        scroller.scrollTo(element, {
            duration: 500,
            delay: 0,
            smooth: 'easeInOutQuart',
            containerId: container
        }));
  }

  let Markers = filteredReports.map((marker, index) => {
    return <Marker
      key={marker.id}
      active={reportIndex === index}
      title={"marker id: " + marker.id}
      position={{ lat: marker.lat, lng: marker.lng }}
      events={{
//        onClick: () => window.alert(`marker ${index} clicked`)
        onClick: () => {
          setCenter({ lat: marker.lat, lng: marker.lng });
          setReportIndex(marker.id);
          scrollToWithContainer('listContainer', 'reportList' + marker.id);
        }
      }}
    />
   });

  let List = filteredReports.map((marker, index) => {
    return <Element name={'reportList' + marker.id} key={marker.id}><ListItem
        key={marker.id}
        name={marker.id}
        id={marker.id}
        active={reportIndex === index}
        lat={marker.lat}
        lng={marker.lng}
        frequency={marker.frequency}
        interference={marker.interference}
        frequency={marker.frequency}
        strength={marker.strength}
        time={timeConverter(marker.time)}
        callsign={marker.callsign}
      /></Element>
  });

  const { data, error, isLoading, isResolved } = useAsync({ promiseFn: loadReports })

  if (isLoading && !isLoaded) {
    return <div>Loading...</div>
  };
  if (error && !isLoaded) {
    return <div>Error...</div>;
  }
  if (data && isResolved && !isLoaded) {
    setReportData(data);
    setFilteredReports(data);
    setIsLoaded(true);
    return <div>Staging data...</div>
  }
  if (isLoaded) {

    Events.scrollEvent.register('begin', function() {
      console.log("begin", arguments);
    });

    Events.scrollEvent.register('end', function() {
      console.log("end", arguments);
    });

    scrollSpy.update();

    return (
      <Container fluid='true' style={{height:'100%', padding:'0px'}}>
        <Row noGutters='true' style={{height:'8%'}}>
          <Navbar bg="light" expand="lg" style={{width:'100%'}}>
            <Navbar.Brand href="#home">Kaptos</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="mr-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#link">About</Nav.Link>
                <NavDropdown title="Reports" id="basic-nav-dropdown">
                  <NavDropdown.Item href="#action/3.1">Last 7 days</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.2">Last 2 Weeks</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.3">Last Month</NavDropdown.Item>
                  <NavDropdown.Divider />
                  <NavDropdown.Item href="#action/3.4">Year to date</NavDropdown.Item>
                </NavDropdown>
              </Nav>
              <Form inline>
                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                <Button variant="outline-success">Search</Button>
              </Form>
            </Navbar.Collapse>
          </Navbar>
        </Row>
        <Row style={{height:'92%'}} noGutters="true">
          <Col xs={6} md={4} id="leftColumn" style={{height:'100%', overflow:'scroll'}}>
            <div id="controlsContainer">
              <div style={{}} id="filterContainer">Future Filter Controls</div>
              <div style={{}} id="infoContainer">Current report id { reportIndex }. { filteredReports.length} visible.</div>
              <div style={{}} id="controlContainer">
                <Button
                  className="btn"
                  onClick={() => setReportIndex((reportIndex + 1) % filteredReports.length)}
                >
                  Next Report
                </Button>
                <Button
                  className="btn"
                  onClick={() => setHeatmapLayerEnabled(!heatmapLayerEnabled)}
                >
                  Toggle heatmap layer
                </Button>
              </div>
            </div>
            <Element id="listContainer">
              {List}
            </Element>

          </Col>
          <Col xs={12} md={8} id="mapContainer" style={{height:'100%'}}>
            <Map
              zoom={ defaults.zoom }
              center={ center }
              events={{ onBoundsChanged: arg => setBounds(arg) }}
            >
              { Markers }
              <HeatmapLayer enabled={heatmapLayerEnabled} />
            </Map>
          </Col>
        </Row>
      </Container>
    );
  }
}
