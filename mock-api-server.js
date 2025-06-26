/**
 * Mock API Server for testing the REST API MCP Server
 * 
 * This simple Express server provides endpoints for testing the query_with_three_params tool.
 */

import express from 'express';
import cors from 'cors';

// Extension class definition
class Extension {
  constructor(code1, code2, code3) {
    this.code1 = code1;
    this.code2 = code2;
    this.code3 = code3;
  }
}

// Product class definition
class Product {
  constructor(id, name, section, subsection, coverage, extension) {
    this.id = id;
    this.name = name;
    this.section = section;
    this.subsection = subsection;
    this.coverage = coverage;
    this.extension = extension;
  }
}

// Configuration object with unique arbitrary values for each product
const CONFIG = {
  "TRE TreMoon Shop": {
    sections: ['ABC', 'XYZ', 'PQR', 'STU', 'VWX'],
    subsection: ['TRE', 'MOO', 'SHO'],
    coverages: ['AKH', 'SVT', 'SAEL', 'QWER', 'ZXCV'],
    extensions: {
      code1: ['T001', 'T002', 'T003', 'T004', 'T005'],
      code2: ['TR01', 'TR02', 'TR03', 'TR04', 'TR05'],
      code3: ['TRE1', 'TRE2', 'TRE3', 'TRE4', 'TRE5']
    }
  },
  "BIL Billon SASKC": {
    sections: ['DEF', 'RST', 'UVW', 'YZA', 'BCD'],
    subsection: ['BIL', 'LON', 'SAS'],
    coverages: ['MNBV', 'HJKL', 'TYUI', 'DFGH', 'POIU'],
    extensions: {
      code1: ['B001', 'B002', 'B003', 'B004', 'B005'],
      code2: ['BL01', 'BL02', 'BL03', 'BL04', 'BL05'],
      code3: ['BIL1', 'BIL2', 'BIL3', 'BIL4', 'BIL5']
    }
  },
  "GAM GameZone Pro": {
    sections: ['GHI', 'EFG', 'HIJ', 'KLM', 'NOP'],
    subsection: ['GAM', 'ZON', 'PRO'],
    coverages: ['LKJH', 'GFDS', 'WERT', 'VCXZ', 'NBMQ'],
    extensions: {
      code1: ['G001', 'G002', 'G003', 'G004', 'G005'],
      code2: ['GM01', 'GM02', 'GM03', 'GM04', 'GM05'],
      code3: ['GAM1', 'GAM2', 'GAM3', 'GAM4', 'GAM5']
    }
  },
  "MED MediCare Plus": {
    sections: ['JKL', 'QRS', 'TUV', 'WXY', 'ZAB'],
    subsection: ['MED', 'CAR', 'PLU'],
    coverages: ['PLMN', 'OKIJ', 'UHYG', 'RFED', 'WSAQ'],
    extensions: {
      code1: ['M001', 'M002', 'M003', 'M004', 'M005'],
      code2: ['MD01', 'MD02', 'MD03', 'MD04', 'MD05'],
      code3: ['MED1', 'MED2', 'MED3', 'MED4', 'MED5']
    }
  },
  "EDU EduTech Solutions": {
    sections: ['MNO', 'CDE', 'FGH', 'IJK', 'LMN'],
    subsection: ['EDU', 'TEC', 'SOL'],
    coverages: ['XZAQ', 'CVER', 'BNMT', 'YUIO', 'HGJK'],
    extensions: {
      code1: ['E001', 'E002', 'E003', 'E004', 'E005'],
      code2: ['ED01', 'ED02', 'ED03', 'ED04', 'ED05'],
      code3: ['EDU1', 'EDU2', 'EDU3', 'EDU4', 'EDU5']
    }
  }
};

// Global products array to avoid duplication
const PRODUCTS = [
  new Product(1, 'TRE TreMoon Shop', 'ABC', 'TRE', 'AKH', new Extension('T001', 'TR01', 'TRE1')),
  new Product(2, 'BIL Billon SASKC', 'DEF', 'BIL', 'MNBV', new Extension('B001', 'BL01', 'BIL1')),
  new Product(3, 'GAM GameZone Pro', 'GHI', 'GAM', 'LKJH', new Extension('G001', 'GM01', 'GAM1')),
  new Product(4, 'MED MediCare Plus', 'JKL', 'MED', 'PLMN', new Extension('M001', 'MD01', 'MED1')),
  new Product(5, 'EDU EduTech Solutions', 'MNO', 'EDU', 'XZAQ', new Extension('E001', 'ED01', 'EDU1'))
];

const app = express();
const PORT = 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Log all requests
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  if (Object.keys(req.query).length > 0) {
    console.log('Query params:', req.query);
  }
  next();
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    message: 'Mock API Server is running',
    endpoints: [
      '/api/query - Test endpoint for query parameters',
      '/api/products - Product listing with section/subsection/coverage filtering',
      '/api/search - Search endpoint'
    ]
  });
});

// Test endpoint for query parameters
app.get('/api/query', (req, res) => {
  // Get all query parameters
  const params = req.query;
  const paramCount = Object.keys(params).length;
  
  res.json({
    success: true,
    message: `Received ${paramCount} query parameters`,
    params: params,
    timestamp: new Date().toISOString()
  });
});

// Product listing endpoint with filtering
app.get('/api/products', (req, res) => {
  const { sort, limit } = req.query;
  
  let filteredProducts = PRODUCTS;
  
  // Sort if provided
  if (sort === 'name') {
    filteredProducts.sort((a, b) => a.name.localeCompare(b.name));
  } else if (sort === 'section') {
    filteredProducts.sort((a, b) => a.section.localeCompare(b.section));
  } else if (sort === 'subsection') {
    filteredProducts.sort((a, b) => a.subsection.localeCompare(b.subsection));
  } else if (sort === 'coverage') {
    filteredProducts.sort((a, b) => a.coverage.localeCompare(b.coverage));
  }
  
  // Apply limit if provided
  if (limit && !isNaN(parseInt(limit))) {
    filteredProducts = filteredProducts.slice(0, parseInt(limit));
  }
  
  res.json({
    success: true,
    filters: { sort, limit },
    count: filteredProducts.length,
    products: filteredProducts
  });
});

// Search endpoint
app.get('/api/search', (req, res) => {
  const { q, type, max_results } = req.query;
  
  if (!q) {
    return res.status(400).json({
      success: false,
      error: 'Search query (q) is required'
    });
  }
  
  // Filter products by search query (check name, section, subsection, coverage, extension codes)
  let results = PRODUCTS.filter(p => {
    const searchText = q.toLowerCase();
    return p.name.toLowerCase().includes(searchText) ||
           p.section.toLowerCase().includes(searchText) ||
           p.subsection.toLowerCase().includes(searchText) ||
           p.coverage.toLowerCase().includes(searchText) ||
           p.extension.code1.toLowerCase().includes(searchText) ||
           p.extension.code2.toLowerCase().includes(searchText) ||
           p.extension.code3.toLowerCase().includes(searchText);
  });
  
  // Apply max_results if provided
  const limit = max_results ? parseInt(max_results) : results.length;
  results = results.slice(0, limit);
  
  // Remove id from products
  const cleanResults = results.map(p => ({
    name: p.name,
    section: p.section,
    subsection: p.subsection,
    coverage: p.coverage,
    extension: {
      code1: p.extension.code1,
      code2: p.extension.code2,
      code3: p.extension.code3
    }
  }));
  
  res.json({
    success: true,
    products: cleanResults
  });
});

// POST endpoint to update product properties
app.post('/api/products/:id', (req, res) => {
  const productId = parseInt(req.params.id);
  const { section, subsection, coverage, extension } = req.body;
  
  // Find the product to update
  const product = PRODUCTS.find(p => p.id === productId);
  
  if (!product) {
    return res.status(404).json({
      success: false,
      error: `Product with id ${productId} not found`
    });
  }
  
  // Store original values
  const originalProduct = { ...product };
  
  // Update properties if provided
  if (section !== undefined) product.section = section;
  if (subsection !== undefined) product.subsection = subsection;
  if (coverage !== undefined) product.coverage = coverage;
  if (extension !== undefined) {
    if (extension.code1 !== undefined) product.extension.code1 = extension.code1;
    if (extension.code2 !== undefined) product.extension.code2 = extension.code2;
    if (extension.code3 !== undefined) product.extension.code3 = extension.code3;
  }
  
  // Validate against CONFIG if needed
  const productConfig = CONFIG[product.name];
  if (productConfig) {
    if (section && !productConfig.sections.includes(section)) {
      return res.status(400).json({
        success: false,
        error: `Invalid section '${section}' for product '${product.name}'. Valid sections: ${productConfig.sections.join(', ')}`
      });
    }
    if (subsection && !productConfig.subsection.includes(subsection)) {
      return res.status(400).json({
        success: false,
        error: `Invalid subsection '${subsection}' for product '${product.name}'. Valid subsection: ${productConfig.subsection.join(', ')}`
      });
    }
    if (coverage && !productConfig.coverages.includes(coverage)) {
      return res.status(400).json({
        success: false,
        error: `Invalid coverage '${coverage}' for product '${product.name}'. Valid coverages: ${productConfig.coverages.join(', ')}`
      });
    }
    if (extension) {
      if (extension.code1 && !productConfig.extensions.code1.includes(extension.code1)) {
        return res.status(400).json({
          success: false,
          error: `Invalid extension code1 '${extension.code1}' for product '${product.name}'. Valid code1: ${productConfig.extensions.code1.join(', ')}`
        });
      }
      if (extension.code2 && !productConfig.extensions.code2.includes(extension.code2)) {
        return res.status(400).json({
          success: false,
          error: `Invalid extension code2 '${extension.code2}' for product '${product.name}'. Valid code2: ${productConfig.extensions.code2.join(', ')}`
        });
      }
      if (extension.code3 && !productConfig.extensions.code3.includes(extension.code3)) {
        return res.status(400).json({
          success: false,
          error: `Invalid extension code3 '${extension.code3}' for product '${product.name}'. Valid code3: ${productConfig.extensions.code3.join(', ')}`
        });
      }
    }
  }
  
  res.json({
    success: true,
    message: `Product ${productId} updated successfully`,
    product: product,
    changes: {
      section: originalProduct.section !== product.section ? { from: originalProduct.section, to: product.section } : null,
      subsection: originalProduct.subsection !== product.subsection ? { from: originalProduct.subsection, to: product.subsection } : null,
      coverage: originalProduct.coverage !== product.coverage ? { from: originalProduct.coverage, to: product.coverage } : null,
      extension: {
        code1: originalProduct.extension.code1 !== product.extension.code1 ? { from: originalProduct.extension.code1, to: product.extension.code1 } : null,
        code2: originalProduct.extension.code2 !== product.extension.code2 ? { from: originalProduct.extension.code2, to: product.extension.code2 } : null,
        code3: originalProduct.extension.code3 !== product.extension.code3 ? { from: originalProduct.extension.code3, to: product.extension.code3 } : null
      }
    },
    timestamp: new Date().toISOString()
  });
});

// POST endpoint to update product properties by name
app.post('/api/products/name/:name', (req, res) => {
  const productName = decodeURIComponent(req.params.name);
  const { section, subsection, coverage, extension } = req.body;
  
  // Find the product to update by name
  const product = PRODUCTS.find(p => p.name === productName);
  
  if (!product) {
    return res.status(404).json({
      success: false,
      error: `Product with name '${productName}' not found`
    });
  }
  
  // Store original values
  const originalProduct = { ...product };
  
  // Update properties if provided
  if (section !== undefined) product.section = section;
  if (subsection !== undefined) product.subsection = subsection;
  if (coverage !== undefined) product.coverage = coverage;
  if (extension !== undefined) {
    if (extension.code1 !== undefined) product.extension.code1 = extension.code1;
    if (extension.code2 !== undefined) product.extension.code2 = extension.code2;
    if (extension.code3 !== undefined) product.extension.code3 = extension.code3;
  }
  
  // Validate against CONFIG if needed
  const productConfig = CONFIG[product.name];
  if (productConfig) {
    if (section && !productConfig.sections.includes(section)) {
      return res.status(400).json({
        success: false,
        error: `Invalid section '${section}' for product '${product.name}'. Valid sections: ${productConfig.sections.join(', ')}`
      });
    }
    if (subsection && !productConfig.subsection.includes(subsection)) {
      return res.status(400).json({
        success: false,
        error: `Invalid subsection '${subsection}' for product '${product.name}'. Valid subsection: ${productConfig.subsection.join(', ')}`
      });
    }
    if (coverage && !productConfig.coverages.includes(coverage)) {
      return res.status(400).json({
        success: false,
        error: `Invalid coverage '${coverage}' for product '${product.name}'. Valid coverages: ${productConfig.coverages.join(', ')}`
      });
    }
    if (extension) {
      if (extension.code1 && !productConfig.extensions.code1.includes(extension.code1)) {
        return res.status(400).json({
          success: false,
          error: `Invalid extension code1 '${extension.code1}' for product '${product.name}'. Valid code1: ${productConfig.extensions.code1.join(', ')}`
        });
      }
      if (extension.code2 && !productConfig.extensions.code2.includes(extension.code2)) {
        return res.status(400).json({
          success: false,
          error: `Invalid extension code2 '${extension.code2}' for product '${product.name}'. Valid code2: ${productConfig.extensions.code2.join(', ')}`
        });
      }
      if (extension.code3 && !productConfig.extensions.code3.includes(extension.code3)) {
        return res.status(400).json({
          success: false,
          error: `Invalid extension code3 '${extension.code3}' for product '${product.name}'. Valid code3: ${productConfig.extensions.code3.join(', ')}`
        });
      }
    }
  }
  
  res.json({
    success: true,
    message: `Product '${productName}' updated successfully`,
    product: product,
    changes: {
      section: originalProduct.section !== product.section ? { from: originalProduct.section, to: product.section } : null,
      subsection: originalProduct.subsection !== product.subsection ? { from: originalProduct.subsection, to: product.subsection } : null,
      coverage: originalProduct.coverage !== product.coverage ? { from: originalProduct.coverage, to: product.coverage } : null,
      extension: {
        code1: originalProduct.extension.code1 !== product.extension.code1 ? { from: originalProduct.extension.code1, to: product.extension.code1 } : null,
        code2: originalProduct.extension.code2 !== product.extension.code2 ? { from: originalProduct.extension.code2, to: product.extension.code2 } : null,
        code3: originalProduct.extension.code3 !== product.extension.code3 ? { from: originalProduct.extension.code3, to: product.extension.code3 } : null
      }
    },
    timestamp: new Date().toISOString()
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Mock API Server running at http://localhost:${PORT}`);
  console.log('Available endpoints:');
  console.log('  GET / - Server info');
  console.log('  GET /api/query - Test endpoint for query parameters');
  console.log('  GET /api/products - Product listing with section/subsection/coverage filtering');
  console.log('    - Filter by: sort (name/section/subsection/coverage), limit');
  console.log('  GET /api/search - Search by name/section/subsection/coverage');
  console.log('    - Parameters: q (required), max_results (optional)');
  console.log('    - Returns: success + clean product objects (no IDs)');
  console.log('  POST /api/products/:id - Update product properties with validation');
  console.log('  POST /api/products/name/:name - Update product properties by name');
  console.log('    - Update: section, subsection, coverage');
  console.log('    - Validates against product-specific CONFIG values');
  
  console.log('\nAvailable Products:');
  console.log('  1: TRE TreMoon Shop - Section: ABC, Subsection: TRE, Coverage: AKH, Extension: {code1: T001, code2: TR01, code3: TRE1}');
  console.log('  2: BIL Billon SASKC - Section: DEF, Subsection: BIL, Coverage: MNBV, Extension: {code1: B001, code2: BL01, code3: BIL1}');
  console.log('  3: GAM GameZone Pro - Section: GHI, Subsection: GAM, Coverage: LKJH, Extension: {code1: G001, code2: GM01, code3: GAM1}');
  console.log('  4: MED MediCare Plus - Section: JKL, Subsection: MED, Coverage: PLMN, Extension: {code1: M001, code2: MD01, code3: MED1}');
  console.log('  5: EDU EduTech Solutions - Section: MNO, Subsection: EDU, Coverage: XZAQ, Extension: {code1: E001, code2: ED01, code3: EDU1}');
  
  console.log('\nExample API Calls:');
  console.log('  GET /api/products?sort=name&limit=3');
  console.log('  GET /api/search?q=TRE&max_results=5');
  console.log('  POST /api/products/1 with body: {"section": "XYZ", "coverage": "SVT"}');
  
  console.log('\nQuery tool examples:');
  console.log('  URL: http://localhost:3000/api/query');
  console.log('  param1: "section=ABC", param2: "subsection=TRE", param3: "coverage=AKH"');
});