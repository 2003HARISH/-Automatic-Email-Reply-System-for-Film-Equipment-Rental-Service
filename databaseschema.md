# Database Schema for Film Equipment Rental Service

This document outlines the database schema for the Film Equipment Rental Service.

## Table: `equipment`

The `equipment` table stores details about the film equipment available for rent.

| Column      | Data Type | Description                           |
|-------------|------------|---------------------------------------|
| `id`        | INTEGER    | Primary key, auto-incremented         |
| `name`      | TEXT       | Name of the equipment                 |
| `availability` | BOOLEAN  | Availability status (True = available, False = not available) |
| `price`     | REAL       | Rental price per day                  |

### Sample Data

Here is some sample data for the `equipment` table:

| id | name         | availability | price |
|----|--------------|--------------|-------|
| 1  | Camera       | True         | 100.0 |
| 2  | Tripod       | False        | 25.0  |
| 3  | Microphone   | True         | 50.0  |
| 4  | Lighting Kit | True         | 75.0  |

### SQL Script

The following SQL script creates the `equipment` table and inserts the sample data:

```sql
-- Create the equipment table
CREATE TABLE IF NOT EXISTS equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    availability BOOLEAN NOT NULL,
    price REAL NOT NULL
);

-- Insert sample data into the equipment table
INSERT INTO equipment (name, availability, price) VALUES
('Camera', True, 100.0),
('Tripod', False, 25.0),
('Microphone', True, 50.0),
('Lighting Kit', True, 75.0);
