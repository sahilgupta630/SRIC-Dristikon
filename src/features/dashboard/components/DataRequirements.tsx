import { motion, AnimatePresence } from 'motion/react';
import { X, Database, Table, FileJson, CheckCircle2, AlertCircle, Info } from 'lucide-react';

interface DataRequirementsProps {
  onClose: () => void;
}

const dataSchemas = [
  {
    category: 'Project Information',
    priority: 'Critical',
    tables: [
      {
        name: 'projects',
        fields: [
          { name: 'project_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique project identifier' },
          { name: 'title', type: 'VARCHAR(500)', required: true, description: 'Project title' },
          { name: 'pi_id', type: 'INT FOREIGN KEY', required: true, description: 'Principal investigator ID' },
          { name: 'department', type: 'VARCHAR(100)', required: true, description: 'Department name' },
          { name: 'start_date', type: 'DATE', required: true, description: 'Project start date' },
          { name: 'end_date', type: 'DATE', required: true, description: 'Project end date' },
          { name: 'funding_amount', type: 'DECIMAL(15,2)', required: true, description: 'Total funding in INR' },
          { name: 'status', type: 'ENUM', required: true, description: 'Status: planning, active, testing, deployed, completed' },
          { name: 'progress_percentage', type: 'INT', required: true, description: 'Completion percentage (0-100)' },
          { name: 'description', type: 'TEXT', required: false, description: 'Detailed project description' },
          { name: 'keywords', type: 'JSON', required: false, description: 'Array of project keywords/tags' }
        ]
      }
    ]
  },
  {
    category: 'Faculty & Researchers',
    priority: 'Critical',
    tables: [
      {
        name: 'faculty',
        fields: [
          { name: 'faculty_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique faculty identifier' },
          { name: 'name', type: 'VARCHAR(200)', required: true, description: 'Full name' },
          { name: 'email', type: 'VARCHAR(200)', required: true, description: 'Email address' },
          { name: 'department', type: 'VARCHAR(100)', required: true, description: 'Department' },
          { name: 'designation', type: 'VARCHAR(100)', required: true, description: 'Professor/Associate/Assistant' },
          { name: 'specialization', type: 'VARCHAR(500)', required: true, description: 'Areas of expertise' },
          { name: 'h_index', type: 'INT', required: false, description: 'H-index score' },
          { name: 'total_projects', type: 'INT', required: false, description: 'Total number of projects' },
          { name: 'total_funding', type: 'DECIMAL(15,2)', required: false, description: 'Total funding received' },
          { name: 'total_patents', type: 'INT', required: false, description: 'Number of patents' },
          { name: 'impact_score', type: 'DECIMAL(5,2)', required: false, description: 'Calculated impact score (0-100)' }
        ]
      }
    ]
  },
  {
    category: 'Financial Data',
    priority: 'Critical',
    tables: [
      {
        name: 'funding_details',
        fields: [
          { name: 'funding_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique funding record' },
          { name: 'project_id', type: 'INT FOREIGN KEY', required: true, description: 'Associated project' },
          { name: 'source', type: 'VARCHAR(200)', required: true, description: 'Funding source/agency' },
          { name: 'amount', type: 'DECIMAL(15,2)', required: true, description: 'Amount in INR' },
          { name: 'date_received', type: 'DATE', required: true, description: 'Date of fund receipt' },
          { name: 'category', type: 'VARCHAR(100)', required: true, description: 'Government/Industry/Internal' }
        ]
      },
      {
        name: 'expenditure',
        fields: [
          { name: 'expense_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique expense record' },
          { name: 'project_id', type: 'INT FOREIGN KEY', required: true, description: 'Associated project' },
          { name: 'amount', type: 'DECIMAL(15,2)', required: true, description: 'Expense amount' },
          { name: 'category', type: 'VARCHAR(100)', required: true, description: 'Equipment/Manpower/Travel etc.' },
          { name: 'date', type: 'DATE', required: true, description: 'Expense date' }
        ]
      }
    ]
  },
  {
    category: 'Patents & IP',
    priority: 'High',
    tables: [
      {
        name: 'patents',
        fields: [
          { name: 'patent_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique patent identifier' },
          { name: 'project_id', type: 'INT FOREIGN KEY', required: false, description: 'Associated project (if any)' },
          { name: 'title', type: 'VARCHAR(500)', required: true, description: 'Patent title' },
          { name: 'inventors', type: 'JSON', required: true, description: 'Array of inventor IDs' },
          { name: 'filing_date', type: 'DATE', required: true, description: 'Date of filing' },
          { name: 'grant_date', type: 'DATE', required: false, description: 'Date of grant (if granted)' },
          { name: 'status', type: 'ENUM', required: true, description: 'Filed/Under Review/Granted/Rejected' },
          { name: 'category', type: 'VARCHAR(100)', required: true, description: 'Technology category' },
          { name: 'patent_number', type: 'VARCHAR(100)', required: false, description: 'Official patent number' }
        ]
      }
    ]
  },
  {
    category: 'Company Collaborations',
    priority: 'High',
    tables: [
      {
        name: 'companies',
        fields: [
          { name: 'company_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique company identifier' },
          { name: 'name', type: 'VARCHAR(200)', required: true, description: 'Company name' },
          { name: 'sector', type: 'VARCHAR(100)', required: true, description: 'Industry sector' },
          { name: 'contact_person', type: 'VARCHAR(200)', required: false, description: 'Primary contact' },
          { name: 'email', type: 'VARCHAR(200)', required: false, description: 'Contact email' }
        ]
      },
      {
        name: 'collaborations',
        fields: [
          { name: 'collab_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique collaboration ID' },
          { name: 'project_id', type: 'INT FOREIGN KEY', required: true, description: 'Associated project' },
          { name: 'company_id', type: 'INT FOREIGN KEY', required: true, description: 'Associated company' },
          { name: 'start_date', type: 'DATE', required: true, description: 'Collaboration start' },
          { name: 'end_date', type: 'DATE', required: false, description: 'Collaboration end (if applicable)' },
          { name: 'type', type: 'VARCHAR(100)', required: true, description: 'Consultancy/Research/Training' },
          { name: 'rating', type: 'DECIMAL(3,1)', required: false, description: 'Partnership rating (0-5)' }
        ]
      }
    ]
  },
  {
    category: 'Deployment & Impact',
    priority: 'High',
    tables: [
      {
        name: 'deployments',
        fields: [
          { name: 'deployment_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique deployment ID' },
          { name: 'project_id', type: 'INT FOREIGN KEY', required: true, description: 'Associated project' },
          { name: 'deployment_date', type: 'DATE', required: true, description: 'Date of deployment' },
          { name: 'location', type: 'VARCHAR(200)', required: true, description: 'Deployment location' },
          { name: 'users_impacted', type: 'INT', required: false, description: 'Number of end users' },
          { name: 'metrics', type: 'JSON', required: false, description: 'Performance metrics data' }
        ]
      }
    ]
  },
  {
    category: 'Publications & Research Output',
    priority: 'Medium',
    tables: [
      {
        name: 'publications',
        fields: [
          { name: 'publication_id', type: 'INT PRIMARY KEY', required: true, description: 'Unique publication ID' },
          { name: 'project_id', type: 'INT FOREIGN KEY', required: false, description: 'Associated project' },
          { name: 'title', type: 'VARCHAR(500)', required: true, description: 'Publication title' },
          { name: 'authors', type: 'JSON', required: true, description: 'Array of author IDs' },
          { name: 'venue', type: 'VARCHAR(300)', required: true, description: 'Journal/Conference name' },
          { name: 'publication_date', type: 'DATE', required: true, description: 'Publication date' },
          { name: 'citations', type: 'INT', required: false, description: 'Citation count' },
          { name: 'doi', type: 'VARCHAR(200)', required: false, description: 'DOI identifier' }
        ]
      }
    ]
  }
];

export function DataRequirements({ onClose }: DataRequirementsProps) {
  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        className="fixed inset-0 bg-black/80 backdrop-blur-sm z-50 flex items-center justify-center p-4"
        onClick={onClose}
      >
        <motion.div
          initial={{ scale: 0.9, y: 20 }}
          animate={{ scale: 1, y: 0 }}
          exit={{ scale: 0.9, y: 20 }}
          onClick={(e) => e.stopPropagation()}
          className="bg-gradient-to-br from-slate-800 to-slate-900 border border-white/20 rounded-2xl shadow-2xl max-w-6xl w-full max-h-[90vh] overflow-hidden"
        >
          {/* Header */}
          <div className="bg-gradient-to-r from-blue-600 to-purple-600 p-6 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Database className="w-8 h-8 text-white" />
              <div>
                <h2 className="text-white">Data Requirements & Schema</h2>
                <p className="text-blue-100 text-sm">Complete database structure for SRIC Analytics Dashboard</p>
              </div>
            </div>
            <button
              onClick={onClose}
              className="p-2 hover:bg-white/20 rounded-lg transition-colors"
            >
              <X className="w-6 h-6 text-white" />
            </button>
          </div>

          {/* Content */}
          <div className="p-6 overflow-y-auto max-h-[calc(90vh-120px)] custom-scrollbar">
            {/* Overview */}
            <div className="mb-6 p-4 bg-blue-500/10 border border-blue-500/30 rounded-lg">
              <div className="flex items-start gap-3">
                <Info className="w-5 h-5 text-blue-400 mt-0.5" />
                <div>
                  <h3 className="text-white mb-2">Overview</h3>
                  <p className="text-slate-300 text-sm mb-2">
                    This dashboard requires comprehensive data from SRIC's existing systems. The schema below defines 
                    the exact structure needed for optimal ML processing and visualization.
                  </p>
                  <p className="text-slate-400 text-sm">
                    <strong>Lead:</strong> Soumya | <strong>Collaborator:</strong> Sahil
                  </p>
                </div>
              </div>
            </div>

            {/* Priority Legend */}
            <div className="flex gap-4 mb-6">
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 bg-red-500 rounded-full" />
                <span className="text-slate-300 text-sm">Critical</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 bg-orange-500 rounded-full" />
                <span className="text-slate-300 text-sm">High</span>
              </div>
              <div className="flex items-center gap-2">
                <div className="w-3 h-3 bg-yellow-500 rounded-full" />
                <span className="text-slate-300 text-sm">Medium</span>
              </div>
            </div>

            {/* Schemas */}
            <div className="space-y-6">
              {dataSchemas.map((schema, index) => (
                <motion.div
                  key={schema.category}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-slate-700/30 border border-white/10 rounded-xl p-6"
                >
                  <div className="flex items-center justify-between mb-4">
                    <div className="flex items-center gap-3">
                      <Table className="w-5 h-5 text-blue-400" />
                      <h3 className="text-white">{schema.category}</h3>
                    </div>
                    <div className={`px-3 py-1 rounded-full text-xs ${
                      schema.priority === 'Critical' ? 'bg-red-500/20 text-red-300 border border-red-500/30' :
                      schema.priority === 'High' ? 'bg-orange-500/20 text-orange-300 border border-orange-500/30' :
                      'bg-yellow-500/20 text-yellow-300 border border-yellow-500/30'
                    }`}>
                      {schema.priority} Priority
                    </div>
                  </div>

                  <div className="space-y-4">
                    {schema.tables.map((table) => (
                      <div key={table.name} className="bg-slate-800/50 rounded-lg p-4">
                        <div className="flex items-center gap-2 mb-3">
                          <FileJson className="w-4 h-4 text-purple-400" />
                          <code className="text-purple-300">{table.name}</code>
                        </div>

                        <div className="space-y-2">
                          {table.fields.map((field) => (
                            <div
                              key={field.name}
                              className="flex items-start gap-3 p-2 bg-slate-900/50 rounded border border-white/5 hover:border-white/10 transition-colors"
                            >
                              {field.required ? (
                                <CheckCircle2 className="w-4 h-4 text-green-400 mt-0.5 flex-shrink-0" />
                              ) : (
                                <AlertCircle className="w-4 h-4 text-slate-500 mt-0.5 flex-shrink-0" />
                              )}
                              <div className="flex-1 min-w-0">
                                <div className="flex items-baseline gap-2 mb-1">
                                  <code className="text-blue-300 text-sm">{field.name}</code>
                                  <code className="text-slate-400 text-xs">{field.type}</code>
                                  {field.required && (
                                    <span className="text-red-400 text-xs">*required</span>
                                  )}
                                </div>
                                <p className="text-slate-400 text-xs">{field.description}</p>
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </motion.div>
              ))}
            </div>

            {/* Integration Notes */}
            <div className="mt-6 p-4 bg-purple-500/10 border border-purple-500/30 rounded-lg">
              <h3 className="text-white mb-3">Integration Notes</h3>
              <ul className="space-y-2 text-slate-300 text-sm">
                <li className="flex items-start gap-2">
                  <span className="text-purple-400 mt-1">•</span>
                  <span>Data should be provided via REST API endpoints or direct database connection</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-purple-400 mt-1">•</span>
                  <span>ML summarization requires project descriptions and recent activities</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-purple-400 mt-1">•</span>
                  <span>Real-time updates recommended for deployment tracking and funding metrics</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-purple-400 mt-1">•</span>
                  <span>Historical data (3-5 years) needed for trend analysis and forecasting</span>
                </li>
              </ul>
            </div>

            {/* Dependencies */}
            <div className="mt-6 p-4 bg-green-500/10 border border-green-500/30 rounded-lg">
              <h3 className="text-white mb-3">Required Dependencies & Installation</h3>
              <div className="bg-slate-900 rounded-lg p-4">
                <pre className="text-green-400 text-sm overflow-x-auto">
{`# Frontend Dependencies (already included)
npm install motion recharts lucide-react

# Backend API Requirements
- RESTful API with endpoints for each data category
- JWT authentication for secure data access
- Rate limiting and caching for performance
- WebSocket support for real-time updates (optional)

# ML/AI Processing (Python backend)
pip install pandas numpy scikit-learn
pip install transformers  # For text summarization
pip install tensorflow   # For advanced ML models

# Database
- PostgreSQL 13+ or MySQL 8+
- Redis for caching
- ElasticSearch for full-text search (optional)`}
                </pre>
              </div>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
}
