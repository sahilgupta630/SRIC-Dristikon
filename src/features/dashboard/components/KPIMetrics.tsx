
import { motion } from 'motion/react';
import { DollarSign, Rocket, Award, Building2, TrendingUp, Users, FileText, Target } from 'lucide-react';
import { useState, useEffect } from 'react';

const kpiData = [
  // 1. Total Funding Sanctioned (Yellow/Orange)
  // Sum of project_value for all currently active projects.
  {
    id: 'total funding sanctioned',
    label: 'Total Funding Sanctioned',
    value: 22647000000,
    prefix: '₹',
    suffix: 'Cr',
    icon: Target,
    gradient: 'from-green-500 to-emerald-600',
    //change: '+22.1%',
    //trend: 'up'
  },
  // 2. Actual Funds Received (Green/Emerald)
  // Sum of receipt_amount from funds_research.csv + funds_consultancy.csv.
  {
    id: 'actual funds received',
    label: 'Actual Funds Received',
    value: 2991100000,
    prefix: '₹',
    suffix: 'Cr',
    icon: DollarSign,
    gradient: 'from-indigo-500 to-blue-600',
    change: '+9.3%',
    trend: 'up'
  },
  // 3. Total Active Projects (Indigo/Blue)
  // Count of unique rows in active_projects.csv
  {
    id: 'total active projects',
    label: 'Total Active Projects',
    value: 2016,
    icon: FileText,
    gradient: 'from-orange-500 to-red-600',
    change: '+0.3%',
    trend: 'up'
  },
  // 4. New Projects Initiated (Blue/Cyan)
  // from summary table
  {
    id: 'new projects initiated',
    label: 'New Projects Initiated',
    value: 579,
    icon: Rocket,
    gradient: 'from-purple-500 to-pink-600',
    //change: '+0.3%',
    //trend: 'up'
  },
  // 5. Active Researchers (Teal/Green)
  // Count of unique Principal Investigators (PIs) currently leading a project.
  {
    id: 'active researchers',
    label: 'Active Researchers',
    value: 775,
    icon: Users,
    gradient: 'from-green-500 to-emerald-600',
    change: '+4.5%',
    trend: 'up'
  },
  // 6. Patents Filed (Purple/Pink)
  // From Patents Filed 2025.csv
  {
    id: 'patents',
    label: 'Patents Filed',
    value: 135,
    icon: Award,
    gradient: 'from-indigo-500 to-blue-600',
    change: '+30.8%',
    trend: 'up'
  },
  // 7. Company Partnerships (Orange/Red)
  // Count of unique Sponsors (Funding Agencies/Companies) listed.
  {
    id: 'companies',
    label: 'Company Partnerships',
    value: 859,
    icon: Building2,
    gradient: 'from-orange-500 to-red-600',
    //change: '+12.4%',
    //trend: 'up'
  },
  // 8. The Collaboration Index (Rose/Purple)
  // Formula: (Projects with Co-PIs / Total Projects) * 100
  {
    id: 'the colloboration index',
    label: 'The Colloboration Index',
    value: 42.06,
    suffix: '%',
    icon: TrendingUp,
    gradient: 'from-purple-500 to-pink-600',
    //change: '+7.2%',
    //trend: 'up'
  }
];

function formatValue(value: number, prefix?: string, suffix?: string): string {
  if (suffix === 'Cr') {
    return `${prefix || ''}${(value / 10000000).toFixed(1)}${suffix}`;
  }
  return `${prefix || ''}${value}${suffix || ''}`;
}

export function KPIMetrics() {
  const [animatedValues, setAnimatedValues] = useState<Record<string, number>>(
    Object.fromEntries(kpiData.map(kpi => [kpi.id, 0]))
  );

  useEffect(() => {
    const timers = kpiData.map((kpi, index) => {
      return setTimeout(() => {
        const duration = 2000;
        const steps = 60;
        const increment = kpi.value / steps;
        let current = 0;

        const interval = setInterval(() => {
          current += increment;
          if (current >= kpi.value) {
            current = kpi.value;
            clearInterval(interval);
          }
          setAnimatedValues(prev => ({ ...prev, [kpi.id]: current }));
        }, duration / steps);
      }, index * 100);
    });

    return () => timers.forEach(clearTimeout);
  }, []);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="mb-8"
    >
      <motion.h2
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ delay: 0.2 }}
        className="text-white mb-6 flex items-center gap-3"
      >
        <span className="w-1.5 h-8 bg-gradient-to-b from-blue-500 to-purple-600 rounded-full" />
        Key Performance Indicators
      </motion.h2>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {kpiData.map((kpi, index) => (
          <motion.div
            key={kpi.id}
            initial={{ opacity: 0, scale: 0.8, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            transition={{ delay: index * 0.1, duration: 0.5 }}
            whileHover={{
              scale: 1.05,
              y: -5,
              transition: { duration: 0.2 }
            }}
            className="relative group"
          >
            <div className="absolute inset-0 bg-gradient-to-br opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-2xl blur-xl from-blue-500/50 to-purple-500/50" />

            <div className="relative bg-gradient-to-br from-slate-800/90 to-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl p-5 shadow-xl">
              <div className="flex items-start justify-between mb-3">
                <motion.div
                  whileHover={{ rotate: 360 }}
                  transition={{ duration: 0.6 }}
                  className={`p-3 bg-gradient-to-br ${kpi.gradient} rounded-xl shadow-lg`}
                >
                  <kpi.icon className="w-6 h-6 text-white" />
                </motion.div>

                <motion.div
                  initial={{ opacity: 0, x: 10 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.3 + index * 0.1 }}
                  className="flex items-center gap-1 px-2 py-1 bg-green-500/20 border border-green-500/30 rounded-lg"
                >
                  <TrendingUp className="w-3 h-3 text-green-400" />
                  <span className="text-green-400 text-xs">{kpi.change}</span>
                </motion.div>
              </div>

              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.4 + index * 0.1 }}
              >
                <p className="text-white mb-1">
                  {formatValue(animatedValues[kpi.id], kpi.prefix, kpi.suffix)}
                </p>
                <p className="text-slate-400 text-sm">{kpi.label}</p>
              </motion.div>

              {/* Animated Progress Bar */}
              <motion.div
                initial={{ scaleX: 0 }}
                animate={{ scaleX: 1 }}
                transition={{ delay: 0.5 + index * 0.1, duration: 0.8 }}
                className={`absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r ${kpi.gradient} rounded-b-2xl origin-left`}
              />
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
}
