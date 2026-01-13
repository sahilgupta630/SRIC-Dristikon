
import { useState, useMemo } from 'react';
import { motion } from 'motion/react';
import { AreaChart, Area, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, Legend } from 'recharts';
import { TrendingUp, TrendingDown, Activity } from 'lucide-react';

// --- CUMULATIVE DATA 2025 (YTD Growth) ---
const monthlyImpactData = [
  { month: 'Jan', funding: 11.4, deployments: 1459, patents: 13, companies: 641, impact: 45.0, new_projects: 38 },
  { month: 'Feb', funding: 34.1, deployments: 1510, patents: 23, companies: 666, impact: 45.2, new_projects: 83 },
  { month: 'Mar', funding: 51.0, deployments: 1541, patents: 48, companies: 688, impact: 45.3, new_projects: 113 },
  { month: 'Apr', funding: 69.8, deployments: 1588, patents: 59, companies: 710, impact: 45.0, new_projects: 160 },
  { month: 'May', funding: 87.2, deployments: 1642, patents: 72, companies: 729, impact: 44.4, new_projects: 214 },
  { month: 'Jun', funding: 118.7, deployments: 1729, patents: 77, companies: 754, impact: 43.5, new_projects: 300 },
  { month: 'Jul', funding: 173.9, deployments: 1787, patents: 81, companies: 778, impact: 42.8, new_projects: 358 },
  { month: 'Aug', funding: 195.0, deployments: 1827, patents: 94, companies: 798, impact: 42.4, new_projects: 398 },
  { month: 'Sep', funding: 224.7, deployments: 1888, patents: 99, companies: 824, impact: 42.1, new_projects: 459 },
  { month: 'Oct', funding: 241.6, deployments: 1930, patents: 109, companies: 834, impact: 41.9, new_projects: 500 },
  { month: 'Nov', funding: 286.6, deployments: 1980, patents: 118, companies: 850, impact: 41.8, new_projects: 550 },
  { month: 'Dec', funding: 299.1, deployments: 2016, patents: 135, companies: 859, impact: 42.1, new_projects: 579 },
];

// --- RADAR DATA: JAN vs DEC (Relative Performance) ---
const radarData = [
  { metric: 'Innovation', jan: 100, dec: 131, fullMark: 150 }, // Patents
  { metric: 'Liquidity', jan: 100, dec: 109, fullMark: 150 }, // Funds
  { metric: 'Talent', jan: 100, dec: 107, fullMark: 150 }, // Researchers
  { metric: 'Volume', jan: 100, dec: 102, fullMark: 150 }, // Active Projects
  { metric: 'Teamwork', jan: 100, dec: 96, fullMark: 150 }, // Collaboration
  { metric: 'Reach', jan: 100, dec: 94, fullMark: 150 }, // Partners
  { metric: 'Scale', jan: 100, dec: 92, fullMark: 150 }, // Portfolio Value
  { metric: 'Pipeline', jan: 100, dec: 76, fullMark: 150 }, // New Projects
];

type MetricType = 'funding' | 'deployments' | 'patents' | 'companies' | 'impact' | 'new_projects';

const metrics: { key: MetricType; label: string; color: string; unit: string }[] = [
  { key: 'funding', label: 'Funding ', color: '#10b981', unit: 'Cr' }, // Emerald
  { key: 'patents', label: 'Patents', color: '#8b5cf6', unit: '' },       // Violet
  { key: 'deployments', label: 'Projects', color: '#3b82f6', unit: '' },  // Blue
  { key: 'companies', label: 'Partners', color: '#f59e0b', unit: '' },      // Amber
  { key: 'new_projects', label: 'Pipeline', color: '#06b6d4', unit: '' },   // Cyan
  { key: 'impact', label: 'Collab %', color: '#ec4899', unit: '%' }         // Pink
];

export function ProjectImpactAnalytics() {
  const [selectedMetric, setSelectedMetric] = useState<MetricType>('funding');
  const [chartType, setChartType] = useState<'area' | 'bar' | 'radar'>('area');

  // Calculate Cumulative Trend (Total YTD Value)
  const trendAnalysis = useMemo(() => {
    if (chartType === 'radar') return { percent: 9.2, isPositive: true }; // General Aggregate

    // For cumulative charts, we compare Current Total vs Start of Year
    const start = monthlyImpactData[0][selectedMetric];
    const current = monthlyImpactData[monthlyImpactData.length - 1][selectedMetric];

    // Growth calculation
    const diff = ((current - start) / start) * 100;

    return {
      percent: Math.abs(diff).toFixed(0),
      isPositive: diff >= 0,
      value: current
    };
  }, [selectedMetric, chartType]);

  const activeColor = metrics.find(m => m.key === selectedMetric)?.color || '#10b981';

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.3, duration: 0.6 }}
      className="bg-gradient-to-br from-slate-800/90 to-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl p-6 shadow-2xl h-full flex flex-col relative overflow-hidden group"
    >
      {/* Hover Glow Effect from KPI style */}
      <div className="absolute inset-0 bg-gradient-to-br opacity-0 group-hover:opacity-10 transition-opacity duration-500 from-blue-500/20 to-purple-500/20 pointer-events-none" />

      {/* Header Section */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-8 gap-4 z-10">
        <div className="flex items-center gap-4">
          <motion.div
            initial={false}
            animate={{ scale: 1 }}
            whileHover={{ scale: 1.05, rotate: 5 }}
            className={`p-3 rounded-xl shadow-lg bg-gradient-to-br ${trendAnalysis.isPositive ? 'from-green-600 to-emerald-600' : 'from-rose-500 to-red-600'
              }`}
          >
            {chartType === 'radar' ? (
              <Activity className="w-6 h-6 text-white" />
            ) : trendAnalysis.isPositive ? (
              <TrendingUp className="w-6 h-6 text-white" />
            ) : (
              <TrendingDown className="w-6 h-6 text-white" />
            )}
          </motion.div>

          <div>
            <h3 className="text-white font-bold text-xl tracking-tight flex items-center gap-2">
              Project Impact Analytics
            </h3>
            <div className="flex items-center gap-3 mt-1">
              <span className="text-slate-400 text-sm font-medium">2025 Cumulative Growth</span>
              {chartType !== 'radar' && (
                <span className={`px-2.5 py-0.5 rounded-lg text-xs font-bold text-white shadow-sm border border-white/10 bg-gradient-to-r ${trendAnalysis.isPositive ? 'from-emerald-500/80 to-green-600/80' : 'from-rose-500/80 to-red-600/80'
                  }`}>
                  Total: {trendAnalysis.value} {metrics.find(m => m.key === selectedMetric)?.unit}
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Chart Toggle */}
        <div className="flex bg-slate-950/50 p-1 rounded-xl border border-white/5 backdrop-blur-md">
          {(['area', 'bar', 'radar'] as const).map((type) => (
            <button
              key={type}
              onClick={() => setChartType(type)}
              className={`px-4 py-1.5 rounded-lg text-xs font-semibold capitalize transition-all duration-300 ${chartType === type
                ? 'bg-slate-800 text-white shadow-md ring-1 ring-white/10'
                : 'text-slate-400 hover:text-slate-200 hover:bg-white/5'
                }`}
            >
              {type}
            </button>
          ))}
        </div>
      </div>

      {/* Metric Selector (Hidden for Radar) */}
      {chartType !== 'radar' && (
        <div className="flex flex-wrap gap-3 mb-8 z-10">
          {metrics.map((metric) => (
            <motion.button
              key={metric.key}
              whileHover={{ scale: 1.02, y: -2 }}
              whileTap={{ scale: 0.98 }}
              onClick={() => setSelectedMetric(metric.key)}
              className={`flex-1 min-w-[110px] px-4 py-3 rounded-xl text-sm border transition-all duration-300 relative overflow-hidden group ${selectedMetric === metric.key
                ? 'bg-slate-800 text-white border-white/20 shadow-lg'
                : 'bg-slate-800/40 text-slate-400 border-white/5 hover:bg-slate-700/60 hover:border-white/10'
                }`}
            >
              {selectedMetric === metric.key && (
                <div
                  className="absolute bottom-0 left-0 right-0 h-1 transition-all duration-300"
                  style={{ backgroundColor: metric.color }}
                />
              )}
              <div className="text-xs font-medium opacity-80 mb-1 tracking-wide uppercase">{metric.label}</div>
              <div className="font-bold text-lg tracking-tight group-hover:text-white transition-colors">
                {monthlyImpactData[11][metric.key]}
                <span className="text-xs ml-1 opacity-60 font-normal">{metric.unit}</span>
              </div>
            </motion.button>
          ))}
        </div>
      )}

      {/* Chart Visualization */}
      <div className="flex-1 min-h-[320px] w-full z-10 bg-slate-950/30 rounded-xl border border-white/5 p-4 backdrop-blur-sm relative">
        <motion.div
          key={`${chartType}-${selectedMetric}`}
          initial={{ opacity: 0, scale: 0.98 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.4 }}
          className="h-full"
        >
          {chartType === 'area' && (
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={monthlyImpactData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
                <defs>
                  <linearGradient id={`gradient-${selectedMetric}`} x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor={activeColor} stopOpacity={0.4} />
                    <stop offset="95%" stopColor={activeColor} stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.1} vertical={false} />
                <XAxis
                  dataKey="month"
                  stroke="#64748b"
                  fontSize={11}
                  tickLine={false}
                  axisLine={false}
                  padding={{ left: 20, right: 20 }}
                  dy={10}
                />
                <YAxis
                  stroke="#64748b"
                  fontSize={11}
                  tickLine={false}
                  axisLine={false}
                  tickFormatter={(value) => `${value}`}
                  dx={-10}
                />
                <Tooltip
                  contentStyle={{
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    borderColor: 'rgba(255,255,255,0.1)',
                    borderRadius: '12px',
                    boxShadow: '0 8px 32px rgba(0,0,0,0.4)'
                  }}
                  itemStyle={{ color: '#e2e8f0', fontWeight: 600 }}
                  labelStyle={{ color: '#94a3b8', marginBottom: '0.25rem', fontSize: '12px' }}
                  cursor={{ stroke: activeColor, strokeWidth: 1, strokeDasharray: '4 4' }}
                />
                <Area
                  type="monotone"
                  dataKey={selectedMetric}
                  stroke={activeColor}
                  strokeWidth={3}
                  fill={`url(#gradient-${selectedMetric})`}
                  activeDot={{ r: 6, strokeWidth: 0, fill: '#fff', stroke: activeColor }}
                  animationDuration={1500}
                />
              </AreaChart>
            </ResponsiveContainer>
          )}

          {chartType === 'bar' && (
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={monthlyImpactData} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" opacity={0.1} vertical={false} />
                <XAxis
                  dataKey="month"
                  stroke="#64748b"
                  fontSize={11}
                  tickLine={false}
                  axisLine={false}
                  padding={{ left: 20, right: 20 }}
                  dy={10}
                />
                <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} dx={-10} />
                <Tooltip
                  cursor={{ fill: '#334155', opacity: 0.2 }}
                  contentStyle={{
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    borderColor: 'rgba(255,255,255,0.1)',
                    borderRadius: '12px'
                  }}
                  itemStyle={{ color: '#e2e8f0', fontWeight: 600 }}
                />
                <Bar
                  dataKey={selectedMetric}
                  fill={activeColor}
                  radius={[6, 6, 0, 0]}
                  animationDuration={1500}
                  maxBarSize={60}
                />
              </BarChart>
            </ResponsiveContainer>
          )}

          {chartType === 'radar' && (
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart cx="50%" cy="50%" outerRadius="70%" data={radarData}>
                <PolarGrid stroke="#334155" opacity={0.3} />
                <PolarAngleAxis dataKey="metric" stroke="#94a3b8" fontSize={11} tick={{ fill: '#cbd5e1' }} />
                <PolarRadiusAxis angle={30} domain={[0, 150]} tick={false} axisLine={false} />

                <Radar
                  name="Baseline (Jan '25)"
                  dataKey="jan"
                  stroke="#64748b"
                  strokeWidth={2}
                  fill="#64748b"
                  fillOpacity={0.1}
                />
                <Radar
                  name="Current (Dec '25)"
                  dataKey="dec"
                  stroke="#10b981"
                  strokeWidth={3}
                  fill="#10b981"
                  fillOpacity={0.4}
                />
                <Legend iconType="circle" wrapperStyle={{ fontSize: '12px', paddingTop: '10px', color: '#94a3b8' }} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    borderColor: 'rgba(255,255,255,0.1)',
                    borderRadius: '12px'
                  }}
                />
              </RadarChart>
            </ResponsiveContainer>
          )}
        </motion.div>
      </div>
    </motion.div>
  );
}