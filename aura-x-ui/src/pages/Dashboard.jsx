import MapPanel from "../components/MapPanel";
import RiskPanel from "../components/RiskPanel";
import IncidentStream from "../components/IncidentStream";
import SimulationViewer from "../components/SimulationViewer";
import IntelligencePacket from "../components/IntelligencePacket";

export default function Dashboard() {
  return (
    <div className="grid grid-cols-12 grid-rows-6 gap-2 h-screen bg-slate-900 text-white p-2">

      {/* HEADER */}
      <div className="col-span-12 row-span-1 bg-slate-800 p-3 rounded-xl">
        <h1 className="text-xl font-bold">🔥 Aura-X Control Room</h1>
        <p className="text-sm text-gray-400">
          Municipal Intelligence • GIS • Simulation • Risk Engine
        </p>
      </div>

      {/* MAP */}
      <div className="col-span-7 row-span-4 bg-slate-800 rounded-xl p-2">
        <MapPanel />
      </div>

      {/* RISK PANEL */}
      <div className="col-span-5 row-span-2 bg-slate-800 rounded-xl p-2">
        <RiskPanel />
      </div>

      {/* INCIDENT STREAM */}
      <div className="col-span-5 row-span-2 bg-slate-800 rounded-xl p-2">
        <IncidentStream />
      </div>

      {/* SIMULATION */}
      <div className="col-span-7 row-span-1 bg-slate-800 rounded-xl p-2">
        <SimulationViewer />
      </div>

      {/* INTELLIGENCE PACKET */}
      <div className="col-span-12 row-span-1 bg-slate-800 rounded-xl p-2">
        <IntelligencePacket />
      </div>

    </div>
  );
}