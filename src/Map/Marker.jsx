import { useEffect } from "react";
import useGoogleMapMarker from "./useGoogleMapMarker";

const activeIcon =
  "/static/tower_icon_1.png";
const inactiveIcon =
  "https://maps.gstatic.com/mapfiles/api-3/images/spotlight-poi2.png";

export default function Marker({
  position,
  type,
  maps,
  map,
  events,
  active = false,
  title
}) {
  const marker = useGoogleMapMarker({
    position,
    type,
    maps,
    map,
    events,
    title
  });

  useEffect(
    () => {
      marker &&
        (active ? marker.setIcon(activeIcon) : marker.setIcon(inactiveIcon));
    },
    [active]
  );

  return null;
}
