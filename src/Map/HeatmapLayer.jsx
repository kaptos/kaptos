import { useEffect, useState } from "react";

export default function HeatmapLayer({ enabled, maps, map }) {
  const [heatmapLayer, setHeatmapLayer] = useState();
  useEffect(() => {
    setHeatmapLayer(new maps.TransitLayer());
  }, []);

  useEffect(
    () => {
      if (heatmapLayer) {
        enabled ? heatmapLayer.setMap(map) : heatmapLayer.setMap(null);
      }
    },
    [enabled]
  );

  return null;
}
