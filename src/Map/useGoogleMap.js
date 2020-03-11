import { useEffect, useState, useRef } from "react";
import GoogleMapsApiLoader from "google-maps-api-loader";

const apiKey = process.env.MAP_API_KEY;

const eventsMapping = {
  onCenterChanged: ["center_changed", map => map.getCenter()],
  onBoundsChanged: ["bounds_changed", map => map.getBounds()]
};

export default function useGoogleMap({ zoom, center, events }) {
  const [mapState, setMapState] = useState({ loading: true });
  const mapRef = useRef();
  useEffect(() => {
    GoogleMapsApiLoader({ apiKey }).then(google => {
      const map = new google.maps.Map(mapRef.current, { zoom, center });
      Object.keys(events).forEach(eventName =>
        map.addListener(eventsMapping[eventName][0], () =>
          events[eventName](eventsMapping[eventName][1](map))
        )
      );

      setMapState({ maps: google.maps, map, loading: false });
    });
  }, []);
  return { mapRef, ...mapState };
}
