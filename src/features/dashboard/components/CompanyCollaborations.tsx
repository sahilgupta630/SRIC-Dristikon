import { motion } from 'motion/react';
import { Handshake, Building2, Globe2, Briefcase, Users } from 'lucide-react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts';

// --- REAL DATA: Top 4 Collaborators + Others ---
const collaboratorData = [
  { name: 'ANRF (National Research)', value: 166, color: '#3b82f6' }, // Blue
  { name: 'SERB (Science Board)', value: 153, color: '#8b5cf6' },    // Violet
  { name: 'SRIC (Seed Grants)', value: 81, color: '#f59e0b' },      // Amber
  { name: 'DST (Science & Tech)', value: 65, color: '#10b981' },    // Emerald
  { name: 'Others (854 Agencies)', value: 394, color: '#475569' },  // Slate
];

export function CompanyCollaborations() {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ delay: 0.6, duration: 0.6 }}
      className="bg-gradient-to-br from-slate-800/90 to-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl p-6 shadow-2xl h-full flex flex-col"
    >
      {/* Header */}
      <div className="flex items-center gap-4 mb-4">
        <motion.div
          whileHover={{ rotate: 10, scale: 1.1 }}
          className="p-3 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-2xl shadow-lg shadow-cyan-500/20"
        >
          <Handshake className="w-6 h-6 text-white stroke-[2.5]" />
        </motion.div>
        <div>
          <h3 className="text-white font-bold text-lg">Collaborator Network</h3>
          <p className="text-slate-400 text-sm font-medium">Top Funding Partners (859 Total)</p>
        </div>
      </div>

      {/* Stats Row */}
      <div className="flex gap-4 mb-5">
        {[
          { label: 'Govt. Agencies', val: '65%', icon: Building2, color: 'text-blue-400' },
          { label: 'Industry', val: '22%', icon: Briefcase, color: 'text-blue-400' },
          { label: 'Global', val: '13%', icon: Globe2, color: 'text-blue-400' },
        ].map((stat) => (
          <div key={stat.label} className="flex-1 bg-slate-800/50 rounded-lg p-3 border border-white/5 flex flex-col items-center justify-center text-center gap-1 group hover:bg-slate-700/50 transition-colors">
            <stat.icon className={`w-4 h-4 ${stat.color} mb-0.5`} />
            <div className="text-white font-bold text-sm leading-none">{stat.val}</div>
            <div className="text-[9px] text-slate-500 font-bold uppercase tracking-wider">{stat.label}</div>
          </div>
        ))}
      </div>

      {/* Pie Chart Visualization */}
      <div className="flex-1 min-h-[300px] relative">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={collaboratorData}
              cx="50%"
              cy="50%"
              innerRadius="60%"
              outerRadius="80%"
              paddingAngle={2}
              dataKey="value"
              stroke="none"
              animationBegin={200}
              animationDuration={1500}
            >
              {collaboratorData.map((entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={entry.color}
                  stroke={index === 4 ? '#334155' : 'none'}
                  strokeWidth={index === 4 ? 1 : 0}
                />
              ))}
            </Pie>
            <Tooltip
              contentStyle={{
                backgroundColor: '#0f172a',
                border: '1px solid #334155',
                borderRadius: '12px',
                boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.5)'
              }}
              itemStyle={{ color: '#e2e8f0', fontSize: '12px', fontWeight: 600 }}
              formatter={(value, name) => [`${value} Projects`, name]}
            />
          </PieChart>
        </ResponsiveContainer>

        {/* Center Text Overlay */}
        <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
          <div className="text-center">
            <div className="text-3xl font-black text-white tracking-tight">859</div>
            <div className="text-[10px] text-slate-400 font-bold uppercase flex items-center justify-center gap-1">
              <Users size={10} /> Partners
            </div>
          </div>
        </div>
      </div>

      {/* Custom Legend List */}
      <div className="grid grid-cols-1 gap-2 mt-4">
        {collaboratorData.slice(0, 4).map((item, index) => (
          <motion.div
            key={item.name}
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.8 + index * 0.1 }}
            className="flex items-center justify-between group p-1.5 hover:bg-white/5 rounded-lg transition-colors"
          >
            <div className="flex items-center gap-3">
              <div
                className="w-3 h-3 rounded-full shadow-lg shadow-black/50"
                style={{ backgroundColor: item.color }}
              />
              <span className="text-slate-300 text-xs font-medium group-hover:text-white transition-colors">
                {item.name}
              </span>
            </div>
            <span className="text-white font-bold text-xs bg-slate-800 px-2 py-0.5 rounded-full border border-white/5">
              {item.value}
            </span>
          </motion.div>
        ))}

        {/* 'Others' Summary Row */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2 }}
          className="flex items-center justify-between p-1.5 mt-1 border-t border-white/5 pt-2"
        >
          <div className="flex items-center gap-3 pl-1">
            <div className="w-2 h-2 rounded-full bg-slate-600" />
            <span className="text-slate-500 text-xs font-medium italic">Remaining 854 agencies</span>
          </div>
          <span className="text-slate-500 text-xs">{collaboratorData[4].value}</span>
        </motion.div>
      </div>
    </motion.div>
  );
}