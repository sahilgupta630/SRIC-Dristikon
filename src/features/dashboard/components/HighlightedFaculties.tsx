import { motion } from 'motion/react';
// import { Users, TrendingUp, Award, ArrowRight, Star, Wallet, Sparkles, Crown } from 'lucide-react';

// --- REAL DATA: Top 4 Principal Investigators (2025) ---
/*
const topProfs = [
  {
    id: 1,
    name: "Prof. V.K. Tewari",
    dept: "Agricultural and Food Engineering",
    funding: "₹251.1 Cr",
    projects: 1,
    trend: "Stable",
    role: "Strategic Lead",
    rank: 1,
    color: "from-orange-400 to-red-500",
    shadow: "shadow-orange-500/20"
  },
  {
    id: 2,
    name: "Prof. R. Mukherjee",
    dept: "Chemical Engineering",
    funding: "₹241.4 Cr",
    projects: 4,
    trend: "Stable",
    role: "Centre Lead",
    rank: 2,
    color: "from-orange-400 to-red-500",
    shadow: "shadow-orange-500/20"
  },
  {
    id: 3,
    name: "Prof. V. Nagarajan",
    dept: "Ocean Engg & Naval Arch",
    funding: "₹110.1 Cr",
    projects: 5,
    trend: "+40%",
    role: "Research Star",
    rank: 3,
    color: "from-orange-400 to-red-500",
    shadow: "shadow-orange-500/20"
  },
  {
    id: 4,
    name: "Prof. S. Chakraborty",
    dept: "Mechanical Engineering",
    funding: "₹50.1 Cr",
    projects: 58,
    trend: "+21%",
    role: "Volume Leader",
    rank: 4,
    color: "from-orange-400 to-red-500",
    shadow: "shadow-blue-500/20"
  }
];
*/

export function HighlightedFaculties() {
  return null;
  /*
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ delay: 0.7, duration: 0.6 }}
      className="bg-gradient-to-br from-slate-900 to-slate-950 border border-white/10 rounded-2xl p-6 shadow-2xl h-full flex flex-col relative overflow-hidden"
    >
      {/* Background Ambient Glow *}
      <div className="absolute top-0 right-0 w-64 h-64 bg-amber-500/5 blur-[80px] rounded-full pointer-events-none" />

      {/* Header *}
      <div className="flex items-center gap-4 mb-8 relative z-10">
        <motion.div
          whileHover={{ rotate: 10, scale: 1.1 }}
          className="p-3 bg-slate-800 rounded-2xl shadow-lg shadow-yellow-500/20 flex items-center justify-center ring-1 ring-white/10"
        >
          <Users className="w-6 h-6 text-yellow-400 fill-yellow-400 stroke-[2.5]" />
        </motion.div>
        <div>
          <h3 className="text-white font-black text-xl tracking-tight">Research Titans</h3>
          <p className="text-slate-400 text-xs font-bold uppercase tracking-wider mt-0.5">Top Funding Magnets (2025)</p>
        </div>
      </div>

      {/* Profile List *}
      <div className="flex-1 grid grid-cols-2 gap-4 relative z-10">
        {topProfs.map((prof, index) => (
          <motion.div
            key={prof.id}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.8 + index * 0.1 }}
            className="group relative"
          >
            {/* Hover Glow Effect Layer *}
            <div className={`absolute -inset-0.5 bg-gradient-to-r ${prof.color} rounded-xl opacity-0 group-hover:opacity-100 blur transition duration-500`} />

            <div className="relative bg-slate-900 border border-white/10 rounded-xl p-4 hover:bg-slate-800 transition-all duration-300 group-hover:border-transparent h-full flex flex-col justify-between">

              {/* TOP ROW: Rank + Identity *}
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center gap-3">
                  {/* Rank Box *}
                  <div className={`w-10 h-10 rounded-lg flex items-center justify-center shadow-inner font-black text-lg bg-slate-800 border-2 border-yellow-400 text-yellow-400 shadow-yellow-500/10`}>
                    {index === 0 ? <Crown size={18} fill="currentColor" /> : `#${prof.rank}`}
                  </div>

                  <div>
                    <h4 className="text-white font-bold text-base tracking-tight group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-white group-hover:to-slate-300 transition-all">
                      {prof.name}
                    </h4>
                    <p className="text-white text-xs font-medium truncate max-w-[140px] transition-colors">
                      {prof.dept}
                    </p>
                  </div>
                </div>

                {/* Role Pill *}
                <div className="px-2.5 py-1 rounded-full bg-white/5 border border-white/5 backdrop-blur-sm group-hover:bg-white/10 transition-colors">
                  <span className={`text-[9px] font-bold uppercase tracking-wider text-white`}>
                    {prof.role}
                  </span>
                </div>
              </div>

              {/* BOTTOM ROW: Metrics Grid *}
              <div className="grid grid-cols-12 gap-2">

                {/* 1. FUNDING (Hero Metric) - Spans 6 cols *}
                <div className="col-span-6 bg-gradient-to-br from-slate-800 to-slate-900 rounded-lg px-4 py-2.5 border border-white/5 group-hover:border-white/10 transition-all relative overflow-hidden">
                  <div className="flex items-center justify-between relative z-10 w-full h-full">
                    <div className="flex items-center gap-3">
                      <Wallet size={12} className="text-yellow-400 fill-yellow-400" />
                      <span className="text-[9px] font-bold uppercase text-white group-hover:text-white">Raised</span>
                    </div>
                    <div className="text-sm font-black tracking-tight text-white">
                      {prof.funding}
                    </div>
                  </div>
                  {/* Subtle shine effect on hover *}
                  <div className="absolute inset-0 bg-white/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
                </div>

                {/* 2. PROJECTS - Spans 3 cols *}
                <div className="col-span-3 bg-slate-800/50 rounded-lg p-2 border border-white/5 flex flex-col justify-center items-center group-hover:bg-slate-800 transition-colors">
                  <Award size={14} className="text-yellow-400 fill-yellow-400 mb-1" />
                  <div className="text-sm font-bold text-white leading-none">{prof.projects}</div>
                  <div className="text-[8px] text-white font-bold uppercase mt-0.5">Projs</div>
                </div>

                {/* 3. TREND - Spans 3 cols *}
                <div className="col-span-3 bg-slate-800/50 rounded-lg p-2 border border-white/5 flex flex-col justify-center items-center group-hover:bg-slate-800 transition-colors">
                  <TrendingUp size={14} className="text-yellow-400 mb-1" />
                  <div className={`text-sm font-bold leading-none text-white`}>
                    {prof.trend}
                  </div>
                  <div className="text-[8px] text-white font-bold uppercase mt-0.5">Growth</div>
                </div>

              </div>
            </div>

            {/* Interactive Arrow (Appears on Hover) *}
            <div className="absolute -right-2 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 group-hover:translate-x-[-12px] transition-all duration-300 pointer-events-none">
              <div className={`p-1.5 rounded-full shadow-lg bg-yellow-400`}>
                <ArrowRight size={14} className="text-black" />
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
  */
}
