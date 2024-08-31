CREATE TABLE member (
    member_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(200) NOT NULL,
    password VARCHAR(30) NOT NULL,
    is_admin SMALLINT NOT NULL DEFAULT 0,
    date_joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(member_id)
);

CREATE TABLE plan (
    plan_id INT NOT NULL AUTO_INCREMENT,
    plan VARCHAR(30) NOT NULL,
    member_id INT NOT NULL,
    date_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(plan_id),
    FOREIGN KEY (member_id) REFERENCES member(member_id)
);

CREATE TABLE category (
    category_id INT NOT NULL AUTO_INCREMENT,
    category VARCHAR(30) NOT NULL,
    date_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(category_id)
);

CREATE TABLE journal (
    journal_id INT NOT NULL AUTO_INCREMENT,
    journal VARCHAR(5) NOT NULL DEFAULT 'cuj',
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    details VARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL DEFAULT 0,
    category_id INT NOT NULL,
    member_id INT NOT NULL,
    plan_id INT NOT NULL,
    PRIMARY KEY(journal_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id),
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (plan_id) REFERENCES plan(plan_id)
);

CREATE TABLE budget (
    budget_id INT NOT NULL AUTO_INCREMENT,
    budget VARCHAR(100) NOT NULL DEFAULT 'Monthly Budget #1',
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    details VARCHAR(50) NOT NULL,
    amount FLOAT NOT NULL DEFAULT 0,
    category_id INT NOT NULL,
    member_id INT NOT NULL,
    plan_id INT NOT NULL,
    PRIMARY KEY(budget_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id),
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (plan_id) REFERENCES plan(plan_id)
);
