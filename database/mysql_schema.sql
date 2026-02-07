-- MySQL Schema Export for AI Enabled Digital Notice Board
-- Author: MCA Major Project
-- Database: digital_notice_board

CREATE DATABASE IF NOT EXISTS digital_notice_board;
USE digital_notice_board;

-- ===========================
-- USERS TABLE (Custom User)
-- ===========================
CREATE TABLE accounts_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT "student",
    is_active BOOLEAN DEFAULT TRUE,
    is_staff BOOLEAN DEFAULT FALSE,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ===========================
-- NOTICES TABLE
-- ===========================
CREATE TABLE notice_notice (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME,
    category VARCHAR(100),
    priority VARCHAR(50),
    created_by_id INT,
    attachment VARCHAR(255),

    FOREIGN KEY (created_by_id)
        REFERENCES accounts_user (id)
        ON DELETE CASCADE
);

-- ===========================
-- AI Predictions Log
-- ===========================
CREATE TABLE ai_engine_predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT,
    predicted_category VARCHAR(100),
    confidence FLOAT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- ===========================
-- DRF API Token Table
-- ===========================
CREATE TABLE api_authtoken (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    token VARCHAR(255) UNIQUE NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES accounts_user(id)
);

-- ===========================
-- Sample Data Insert
-- ===========================
INSERT INTO accounts_user (username, email, password, role)
VALUES
("admin", "admin@example.com", "admin123", "admin");

INSERT INTO notice_notice (title, content, category, priority, created_by_id)
VALUES
("Welcome Notice", "Welcome to AI Digital Notice Board", "General", "High", 1);
