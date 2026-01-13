import { useState, useEffect } from 'react';
import { motion } from 'motion/react';
import { BarChart, Bar, LineChart, Line, AreaChart, Area, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { TrendingUp, Users, FileText, DollarSign, Activity } from 'lucide-react';

const monthlyData = [
  { month: 'Jan', proposals: 12, consultancy: 8, funding: 45 },
  { month: 'Feb', proposals: 19, consultancy: 12, funding: 62 },
  { month: 'Mar', proposals: 15, consultancy: 10, funding: 55 },
  { month: 'Apr', proposals: 22, consultancy: 15, funding: 78 },
  { month: 'May', proposals: 28, consultancy: 18, funding: 92 },
  { month: 'Jun', proposals: 25, consultancy: 20, funding: 85 }
];

const categoryData = [
  { name: 'Engineering', value: 35, color: '#3b82f6' },
  { name: 'Science', value: 25, color: '#8b5cf6' },
  { name: 'Technology', value: 20, color: '#10b981' },
  { name: 'Management', value: 15, color: '#f59e0b' },
  { name: 'Others', value: 5, color: '#6b7280' }
];

const stats = [
  { label: 'Active Projects', value: 156, icon: FileText, color: 'bg-blue-500', change: '+12%' },
  { label: 'Total Funding', value: '₹45.2Cr', icon: DollarSign, color: 'bg-green-500', change: '+18%' },
  { label: 'Researchers', value: 234, icon: Users, color: 'bg-purple-500', change: '+8%' },
  { label: 'Success Rate', value: '89%', icon: TrendingUp, color: 'bg-amber-500', change: '+5%' }
];

export function PerformanceMetrics() {
  const [animatedStats, setAnimatedStats] = useState(stats.map(s => ({
    ...s,
    displayValue: typeof s.value === 'number' ? 0 : s.value
  })));
  const [selectedMetric, setSelectedMetric] = useState<'proposals' | 'consultancy' | 'funding'>('proposals');

  useEffect(() => {
    // Animate stat numbers
    const timer = setTimeout(() => {
      setAnimatedStats(stats.map(s => ({ ...s, displayValue: s.value })));
    }, 500);
    return () => clearTimeout(timer);
  }, []);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.2 }}
      className="space-y-6"
    >
      {/* Stats Grid */}
      <div className="grid grid-cols-2 gap-4">
        {stats.map((stat, index) => (
          <motion.div
            key={stat.label}
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3 + index * 0.1, duration: 0.4 }}
            whileHover={{ scale: 1.05 }}
            className="bg-white rounded-xl shadow-lg p-4 relative overflow-hidden"
          >
            <div className="relative z-10">
              <div className="flex items-center justify-between mb-2">
                <div className={`${stat.color} p-2 rounded-lg`}>
                  <stat.icon className="w-5 h-5 text-white" />
                </div>
                <motion.span
                  initial={{ opacity: 0, x: 10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.5 + index * 0.1 }}
                  className="text-green-600"
                >
                  {stat.change}
                </motion.span>
              </div>
              <motion.p
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.4 + index * 0.1 }}
                className="text-slate-900 mb-1"
              >
                {typeof stat.value === 'number' ? animatedStats[index].displayValue : stat.value}
              </motion.p>
              <p className="text-slate-600 text-sm">{stat.label}</p>
            </div>
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: 1 }}
              transition={{ delay: 0.6 + index * 0.1, duration: 0.6 }}
              className={`absolute -bottom-2 -right-2 w-20 h-20 ${stat.color} opacity-10 rounded-full`}
            />
          </motion.div>
        ))}
      </div>

      {/* Main Charts */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.7 }}
        className="bg-white rounded-xl shadow-lg p-6"
      >
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-indigo-100 rounded-lg">
              <Activity className="w-6 h-6 text-indigo-600" />
            </div>
            <div>
              <h3 className="text-slate-900">Monthly Performance</h3>
              <p className="text-slate-600 text-sm">Last 6 months overview</p>
            </div>
          </div>
          <div className="flex gap-2">
            {(['proposals', 'consultancy', 'funding'] as const).map((metric) => (
              <button
                key={metric}
                onClick={() => setSelectedMetric(metric)}
                className={`px-3 py-1.5 rounded-lg capitalize transition-colors ${selectedMetric === metric
                  ? 'bg-indigo-600 text-white'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                  }`}
              >
                {metric}
              </button>
            ))}
          </div>
        </div>

        <motion.div
          key={selectedMetric}
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.4 }}
        >
          <ResponsiveContainer width="100%" height={250}>
            <AreaChart data={monthlyData}>
              <defs>
                <linearGradient id="colorMetric" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#6366f1" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#6366f1" stopOpacity={0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
              <XAxis dataKey="month" stroke="#64748b" />
              <YAxis stroke="#64748b" />
              <Tooltip
                contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '8px', color: '#fff' }}
              />
              <Area
                type="monotone"
                dataKey={selectedMetric}
                stroke="#6366f1"
                strokeWidth={3}
                fill="url(#colorMetric)"
                animationDuration={1000}
              />
            </AreaChart>
          </ResponsiveContainer>
        </motion.div>
      </motion.div>

      {/* Category Distribution */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.9 }}
        className="bg-white rounded-xl shadow-lg p-6"
      >
        <h3 className="text-slate-900 mb-4">Research Category Distribution</h3>
        <div className="flex items-center gap-6">
          <ResponsiveContainer width="50%" height={200}>
            <PieChart>
              <Pie
                data={categoryData}
                cx="50%"
                cy="50%"
                innerRadius={50}
                outerRadius={80}
                paddingAngle={5}
                dataKey="value"
                animationBegin={900}
                animationDuration={1000}
              >
                {categoryData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>

          <div className="flex-1 space-y-2">
            {categoryData.map((category, index) => (
              <motion.div
                key={category.name}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 1.1 + index * 0.1 }}
                className="flex items-center gap-3"
              >
                <div
                  className="w-4 h-4 rounded"
                  style={{ backgroundColor: category.color }}
                />
                <div className="flex-1">
                  <div className="flex justify-between">
                    <span className="text-slate-700">{category.name}</span>
                    <span className="text-slate-900">{category.value}%</span>
                  </div>
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${category.value}%` }}
                    transition={{ delay: 1.2 + index * 0.1, duration: 0.8 }}
                    className="h-1.5 rounded-full mt-1"
                    style={{ backgroundColor: category.color, opacity: 0.3 }}
                  />
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </motion.div>

      {/* Comparison Chart */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 1.1 }}
        className="bg-white rounded-xl shadow-lg p-6"
      >
        <h3 className="text-slate-900 mb-4">Comparative Analysis</h3>
        <ResponsiveContainer width="100%" height={250}>
          <BarChart data={monthlyData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
            <XAxis dataKey="month" stroke="#64748b" />
            <YAxis stroke="#64748b" />
            <Tooltip
              contentStyle={{ backgroundColor: '#1e293b', border: 'none', borderRadius: '8px', color: '#fff' }}
            />
            <Legend />
            <Bar dataKey="proposals" fill="#3b82f6" radius={[8, 8, 0, 0]} animationDuration={1000} />
            <Bar dataKey="consultancy" fill="#8b5cf6" radius={[8, 8, 0, 0]} animationDuration={1200} />
          </BarChart>
        </ResponsiveContainer>
      </motion.div>
    </motion.div>
  );
}
