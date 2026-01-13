import { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { MessageCircle, Send, Search, ChevronDown, CheckCircle2, Clock } from 'lucide-react';

interface Query {
  id: string;
  question: string;
  answer: string;
  status: 'pending' | 'answered';
  timestamp: Date;
  category: string;
}

const mockQueries: Query[] = [
  {
    id: '1',
    question: 'What is the process for submitting a research proposal?',
    answer: 'Research proposals should be submitted through the SRIC portal. Please ensure all required documents including project synopsis, budget estimation, and CVs of principal investigators are attached.',
    status: 'answered',
    timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000),
    category: 'Research Proposals'
  },
  {
    id: '2',
    question: 'How can I apply for industry consultancy projects?',
    answer: 'Industry consultancy applications can be initiated by contacting SRIC office. Faculty members need to submit a brief project outline and timeline for approval.',
    status: 'answered',
    timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000),
    category: 'Consultancy'
  },
  {
    id: '3',
    question: 'What are the funding opportunities available for collaborative research?',
    answer: '',
    status: 'pending',
    timestamp: new Date(Date.now() - 30 * 60 * 1000),
    category: 'Funding'
  }
];

export function QueryHandler() {
  const [queries, setQueries] = useState<Query[]>(mockQueries);
  const [newQuery, setNewQuery] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [expandedQuery, setExpandedQuery] = useState<string | null>(null);

  const categories = ['All', 'Research Proposals', 'Consultancy', 'Funding', 'General'];

  const handleSubmitQuery = () => {
    if (!newQuery.trim()) return;

    const query: Query = {
      id: Date.now().toString(),
      question: newQuery,
      answer: '',
      status: 'pending',
      timestamp: new Date(),
      category: 'General'
    };

    setQueries([query, ...queries]);
    setNewQuery('');
  };

  const filteredQueries = queries.filter(q => {
    const matchesSearch = q.question.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesCategory = selectedCategory === 'All' || q.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="bg-white rounded-2xl shadow-lg p-6 h-fit"
    >
      <div className="flex items-center gap-3 mb-6">
        <div className="p-2 bg-blue-100 rounded-lg">
          <MessageCircle className="w-6 h-6 text-blue-600" />
        </div>
        <div>
          <h2 className="text-slate-900">Query Management</h2>
          <p className="text-slate-600">Submit and track your queries</p>
        </div>
      </div>

      {/* New Query Input */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="mb-6"
      >
        <div className="flex gap-2">
          <input
            type="text"
            value={newQuery}
            onChange={(e) => setNewQuery(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSubmitQuery()}
            placeholder="Ask a question about research or consultancy..."
            className="flex-1 px-4 py-3 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSubmitQuery}
            className="px-4 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </motion.div>

      {/* Search and Filter */}
      <div className="mb-4 space-y-3">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search queries..."
            className="w-full pl-10 pr-4 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div className="flex gap-2 overflow-x-auto pb-2">
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => setSelectedCategory(category)}
              className={`px-4 py-1.5 rounded-full whitespace-nowrap transition-colors ${
                selectedCategory === category
                  ? 'bg-blue-600 text-white'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              {category}
            </button>
          ))}
        </div>
      </div>

      {/* Queries List */}
      <div className="space-y-3 max-h-[600px] overflow-y-auto">
        <AnimatePresence>
          {filteredQueries.map((query, index) => (
            <motion.div
              key={query.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 20 }}
              transition={{ delay: index * 0.1 }}
              className="border border-slate-200 rounded-lg p-4 hover:shadow-md transition-shadow"
            >
              <div
                className="flex items-start justify-between cursor-pointer"
                onClick={() => setExpandedQuery(expandedQuery === query.id ? null : query.id)}
              >
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-2">
                    <span className="px-2 py-0.5 bg-slate-100 text-slate-700 rounded text-sm">
                      {query.category}
                    </span>
                    {query.status === 'answered' ? (
                      <CheckCircle2 className="w-4 h-4 text-green-600" />
                    ) : (
                      <Clock className="w-4 h-4 text-amber-600" />
                    )}
                  </div>
                  <p className="text-slate-900">{query.question}</p>
                  <p className="text-slate-500 text-sm mt-1">
                    {query.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </p>
                </div>
                <motion.div
                  animate={{ rotate: expandedQuery === query.id ? 180 : 0 }}
                  transition={{ duration: 0.3 }}
                >
                  <ChevronDown className="w-5 h-5 text-slate-400" />
                </motion.div>
              </div>

              <AnimatePresence>
                {expandedQuery === query.id && query.answer && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                    className="mt-3 pt-3 border-t border-slate-200"
                  >
                    <p className="text-slate-700">{query.answer}</p>
                  </motion.div>
                )}
                {expandedQuery === query.id && !query.answer && (
                  <motion.div
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    transition={{ duration: 0.3 }}
                    className="mt-3 pt-3 border-t border-slate-200"
                  >
                    <p className="text-amber-600">This query is pending review by SRIC team.</p>
                  </motion.div>
                )}
              </AnimatePresence>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>
    </motion.div>
  );
}
