import { motion } from 'motion/react';
import { Award, TrendingUp, Lightbulb } from 'lucide-react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, BarChart, Bar, XAxis, YAxis, CartesianGrid } from 'recharts';

// --- REAL DATA: Top Innovating Departments (2025) ---
const patentByCategory = [
  { name: 'CSE', value: 24, color: '#3b82f6' },   // Blue
  { name: 'ECE', value: 18, color: '#8b5cf6' },   // Violet
  { name: 'SMST', value: 15, color: '#10b981' },  // Emerald
  { name: 'CY', value: 13, color: '#f59e0b' },    // Amber
  { name: 'GSSST', value: 12, color: '#ec4899' }, // Pink
  { name: 'Others', value: 53, color: '#64748b' } // Slate
];

// --- REAL DATA: Filing Trend ---
const patentTimeline = [
  { year: '2020', filed: 85, granted: 42 },
  { year: '2021', filed: 92, granted: 58 },
  { year: '2022', filed: 104, granted: 65 },
  { year: '2023', filed: 118, granted: 78 },
  { year: '2024', filed: 126, granted: 85 },
  { year: '2025', filed: 135, granted: 91 }
];

export function PatentAnalytics() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.5, duration: 0.6 }}
      className="bg-gradient-to-br from-slate-800/90 to-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl p-6 shadow-2xl h-full flex flex-col relative overflow-hidden group"
    >
      {/* Hover Glow Effect */}
      <div className="absolute inset-0 bg-gradient-to-br opacity-0 group-hover:opacity-10 transition-opacity duration-500 from-violet-500/20 to-fuchsia-500/20 pointer-events-none" />

      {/* Header */}
      <div className="flex items-center gap-4 mb-6 z-10 shrink-0">
        <motion.div
          whileHover={{ rotate: 360, scale: 1.1 }}
          transition={{ duration: 0.6 }}
          className="p-3 bg-gradient-to-br from-blue-600 to-blue-800 rounded-2xl shadow-lg border border-blue-400"
        >
          <Award className="w-6 h-6 text-white stroke-[2.5]" />
        </motion.div>
        <div>
          <h3 className="text-white font-bold text-xl tracking-tight">Patent Analytics</h3>
          <p className="text-slate-400 text-sm font-medium">IP & Innovation Report 2025</p>
        </div>
      </div>

      <div className="grid md:grid-cols-2 gap-8 z-10 mb-4 flex-1">
        
        {/* --- PIE CHART SECTION --- */}
        <div className="flex flex-col bg-slate-950/30 rounded-2xl p-4 border border-white/5 min-h-[300px]">
          <h4 className="text-slate-300 text-sm font-bold mb-2 flex items-center gap-2 uppercase tracking-wide shrink-0">
            <Lightbulb size={14} className="text-amber-400" />
            Innovation by Dept.
          </h4>
          
          {/* Chart Area - Now MAXIMIZED using Percentages */}
          <div className="flex-1 min-h-0 relative -mx-4">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={patentByCategory}
                  cx="50%"
                  cy="50%"
                  innerRadius="60%"  // Changed from fixed 45 to percentage
                  outerRadius="80%"  // Changed from fixed 65 to percentage
                  paddingAngle={3}
                  dataKey="value"
                  stroke="none"
                  animationBegin={200}
                  animationDuration={1500}
                >
                  {patentByCategory.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} stroke="rgba(0,0,0,0.2)" strokeWidth={1} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    borderColor: 'rgba(255,255,255,0.1)',
                    borderRadius: '12px',
                    boxShadow: '0 8px 32px rgba(0,0,0,0.4)',
                    backdropFilter: 'blur(8px)'
                  }}
                  itemStyle={{ color: '#e2e8f0', fontSize: '12px', fontWeight: 600 }}
                />
              </PieChart>
            </ResponsiveContainer>
            
            {/* Center Stat */}
            <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
              <div className="text-center">
                 <div className="text-4xl font-black text-white tracking-tighter">135</div>
                 <div className="text-[10px] text-slate-400 font-bold uppercase tracking-widest">Filed</div>
              </div>
            </div>
          </div>

          {/* COMPACT 3-COLUMN LEGEND */}
          <div className="grid grid-cols-3 gap-2 mt-2 shrink-0">
            {patentByCategory.map((category, index) => (
              <motion.div
                key={category.name}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.7 + index * 0.05 }}
                className="flex items-center gap-1.5 bg-slate-800/40 p-1.5 rounded border border-white/5 hover:bg-slate-800/60 transition-colors"
              >
                <div
                  className="w-1.5 h-1.5 rounded-full ring-1 ring-white/10 shrink-0"
                  style={{ backgroundColor: category.color }}
                />
                <div className="flex flex-col leading-none min-w-0">
                  <span className="text-slate-300 text-[9px] font-bold truncate">{category.name}</span>
                  <span className="text-white text-[9px] opacity-70">{category.value}</span>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* --- BAR CHART SECTION --- */}
        <div className="flex flex-col bg-slate-950/30 rounded-2xl p-4 border border-white/5 min-h-[300px]">
          <h4 className="text-slate-300 text-sm font-bold mb-4 flex items-center gap-2 uppercase tracking-wide shrink-0">
            <TrendingUp size={14} className="text-emerald-400" />
            Yearly Filing Trend
          </h4>
          <div className="flex-1 min-h-0">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={patentTimeline} margin={{ top: 10, right: 0, left: -25, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.1} vertical={false} />
                <XAxis
                  dataKey="year"
                  stroke="#64748b"
                  fontSize={10}
                  tickLine={false}
                  axisLine={false}
                  dy={10}
                />
                <YAxis
                  stroke="#64748b"
                  fontSize={10}
                  tickLine={false}
                  axisLine={false}
                />
                <Tooltip
                  cursor={{ fill: '#334155', opacity: 0.2 }}
                  contentStyle={{
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    borderColor: 'rgba(255,255,255,0.1)',
                    borderRadius: '12px',
                    boxShadow: '0 8px 32px rgba(0,0,0,0.4)',
                    backdropFilter: 'blur(8px)'
                  }}
                  labelStyle={{ color: '#94a3b8', marginBottom: '0.2rem', fontSize: '12px' }}
                />
                <Bar
                  dataKey="filed"
                  name="Filed"
                  fill="#8b5cf6"
                  radius={[4, 4, 0, 0]}
                  barSize={16}
                  animationDuration={1500}
                />
                <Bar
                  dataKey="granted"
                  name="Granted"
                  fill="#10b981"
                  radius={[4, 4, 0, 0]}
                  barSize={16}
                  animationDuration={1500}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>

          <div className="flex justify-center gap-6 mt-4 shrink-0">
            <div className="flex items-center gap-2">
              <div className="w-2.5 h-2.5 bg-violet-500 rounded-sm" />
              <span className="text-slate-400 text-xs font-medium">Filed</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-2.5 h-2.5 bg-emerald-500 rounded-sm" />
              <span className="text-slate-400 text-xs font-medium">Granted</span>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Stats Row */}
      <div className="grid grid-cols-3 gap-4 border-t border-white/10 pt-4 mt-auto z-10 shrink-0">
        {[
          { label: 'Total 2025', value: '135', sub: 'Filed', change: '+30.8%', trend: 'up' },
          { label: 'Top Dept', value: 'CSE', sub: '24 Patents', change: 'Leader', trend: 'neutral' },
          { label: 'Dec Spike', value: '17', sub: 'New Filings', change: '+88%', trend: 'up' }
        ].map((stat, index) => (
          <motion.div
            key={stat.label}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.9 + index * 0.1 }}
            className="text-center group/stat hover:bg-white/5 rounded-xl py-2 transition-colors cursor-default"
          >
            <p className="text-white font-black text-2xl tracking-tight group-hover/stat:scale-105 transition-transform duration-300">{stat.value}</p>
            <p className="text-slate-500 text-[10px] font-bold uppercase tracking-widest mb-1.5">{stat.label}</p>

            <div className={`flex items-center justify-center gap-1.5 text-xs font-bold px-2 py-0.5 rounded-full inline-flex text-white ${stat.trend === 'up'
              ? 'bg-emerald-500/20 border border-emerald-500/30'
              : 'bg-amber-500/20 border border-amber-500/30'
              }`}>
              {stat.trend === 'up' && <TrendingUp className="w-3 h-3 text-white" />}
              <span>{stat.change}</span>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
}