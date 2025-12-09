-- USERS: customers + admins
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK (role IN ('user','admin'))
);

-- USER CART
CREATE TABLE IF NOT EXISTS cart_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  inventory_id INTEGER NOT NULL,
  UNIQUE(user_id, inventory_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (inventory_id) REFERENCES inventory(id)
);



-- INVENTORY: all pieces, including sold status
CREATE TABLE IF NOT EXISTS inventory (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  era TEXT,
  price REAL NOT NULL,
  description TEXT,
  provenance TEXT,
  image TEXT,
  is_sold INTEGER NOT NULL DEFAULT 0
);

-- ORDERS
CREATE TABLE IF NOT EXISTS orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created_at TEXT NOT NULL,
  subtotal REAL NOT NULL,
  tax REAL NOT NULL,
  shipping REAL NOT NULL,
  total REAL NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- ORDER ITEMS
CREATE TABLE IF NOT EXISTS order_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id INTEGER NOT NULL,
  inventory_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  era TEXT,
  price REAL NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(id),
  FOREIGN KEY (inventory_id) REFERENCES inventory(id)
);

-- Seed admin user (password: admin123) 
INSERT OR IGNORE INTO users (id, name, email, password_hash, role)
VALUES (
  1,
  'Admin',
  'admin@example.com',
  'scrypt:32768:8:1$0AfE0PJfEeE4XyCe$259a1be027ffa28240fb1d7ba11af7f8b59f18fa2d87b1a61a454a142f08f222e0cdc6e0accebe1965bfa092127607607f50a2decb6e9bfd2e6840e923fe2540', 
  'admin'
);

-- Seeded regular user (password: user123)
INSERT INTO users (name, email, password_hash, role)
VALUES (
    'Test User',
    'user@example.com',
    'scrypt:32768:8:1$661sj8kSA1vso998$8719a599aff78a5e405622e4a39779c81b09c45fb57ac9c8354f9bf0dd82c10ea07e692d40ed28ba3b741c37c305b44d3245a73aee991557b24aa207bc092bc3', 
    'user'
);


-- seed inventory data
INSERT INTO inventory (id, title, era, price, description, provenance, image, is_sold) VALUES
(1, 'Golden Horizon', 'Egypt, 1500 BC', 4500, 'A rare artifact symbolizing Egypt’s devotion to the sun god Aten.', 'Verified by the Egyptian Antiquities Authority', '1.jpg', 0),
(2, 'Echoes of Silence', 'Greece, 400 BC', 2800, 'An ode to Greek philosophy and tranquility.', 'Recovered from Aegean region', '2.jpg', 0),
(3, 'Twilight Sonata', 'Florence, 1600 AD', 3600, 'An Italian fresco fragment showing divine symmetry.', 'Discovered near Florence', '3.jpg', 0),
(4, 'Marble Dreams', 'Rome, 200 AD', 5200, 'Carved during the Roman Empire, capturing human perfection.', 'Sourced from the ruins of Ostia Antica', '4.jpg', 0),
(5, 'Whispers of Light', 'Japan, Edo Period', 3200, 'Traditional Japanese minimalism scroll.', 'Acquired through Kyoto estate sale', '5.jpg', 0),
(6, 'Sands of Time', 'Mesopotamia, 1200 BC', 4100, 'Ancient Mesopotamian relic symbolizing history and culture.', 'Recovered from archaeological site', '6.jpg', 0),
(7, 'Crimson Veil', 'Paris, 1850 AD', 4800, 'A romantic depiction of 19th century French art.', 'Preserved in private Parisian collection', '7.jpg', 0),
(8, 'Silent Meadow', 'China, Tang Dynasty', 3950, 'Elegant brushwork from the Tang Dynasty era.', 'Discovered in a preserved temple archive', '8.jpg', 0),
(9, 'Azure Reverie', 'Persia, 500 AD', 2900, 'Persian artistry representing spiritual harmony.', 'Sourced from ancient Persian estate', '9.jpg', 0),
(10, 'Garden of Stillness', 'India, Mughal Empire', 4700, 'Mughal-era painting showing serenity in nature.', 'Recovered from Mughal heritage site', '10.jpg', 0),
(11, 'Chasing Dusk', 'Venice, 1700 AD', 3400, 'Venetian artwork capturing evening tranquility.', 'From a Venetian noble family archive', '11.jpg', 0),
(12, 'Celestial Bloom', 'Egypt, 3100 BC', 5000, 'Rare early dynastic artifact representing rebirth.', 'Authenticated by Cairo Museum specialists', '12.jpg', 0);
