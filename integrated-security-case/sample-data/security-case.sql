CREATE TABLE signin_events (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    username TEXT,
    source_ip TEXT,
    application TEXT,
    status TEXT,
    error_code INTEGER
);

INSERT INTO signin_events VALUES
(1, '2026-09-10 08:14:02', 'emma.lee@northstar.example', '198.51.100.23', 'OfficeHome', 'failed', 50126),
(2, '2026-09-10 08:14:11', 'emma.lee@northstar.example', '198.51.100.23', 'OfficeHome', 'failed', 50126),
(3, '2026-09-10 08:14:20', 'emma.lee@northstar.example', '198.51.100.23', 'OfficeHome', 'failed', 50126),
(4, '2026-09-10 08:14:32', 'emma.lee@northstar.example', '198.51.100.23', 'OfficeHome', 'failed', 50126),
(5, '2026-09-10 08:14:47', 'emma.lee@northstar.example', '198.51.100.23', 'OfficeHome', 'failed', 50126),
(6, '2026-09-10 08:15:03', 'emma.lee@northstar.example', '198.51.100.23', 'OfficeHome', 'failed', 50126),
(7, '2026-09-10 08:15:19', 'emma.lee@northstar.example', '198.51.100.23', 'OfficeHome', 'success', 0),
(8, '2026-09-10 08:16:02', 'emma.lee@northstar.example', '198.51.100.23', 'Outlook Web', 'success', 0),
(9, '2026-09-10 08:17:41', 'emma.lee@northstar.example', '198.51.100.23', 'My Profile', 'success', 0),
(10, '2026-09-10 08:22:10', 'daniel.ross@northstar.example', '10.10.20.15', 'OfficeHome', 'success', 0),
(11, '2026-09-10 08:31:44', 'sophia.kim@northstar.example', '10.10.20.21', 'Outlook Web', 'success', 0),
(12, '2026-09-10 08:42:05', 'emma.lee@northstar.example', '10.10.20.33', 'OfficeHome', 'success', 0);


CREATE TABLE assets (
    asset_id INTEGER PRIMARY KEY,
    asset_name TEXT,
    asset_type TEXT,
    owner TEXT,
    criticality TEXT
);

INSERT INTO assets VALUES
(1, 'Customer Database', 'Database', 'Data Team', 'Critical'),
(2, 'Microsoft 365 Tenant', 'Cloud Identity', 'IT', 'High'),
(3, 'Linux Web Server', 'Server', 'Web Team', 'High'),
(4, 'Corporate Email', 'Cloud Service', 'IT', 'High'),
(5, 'Remote Administration', 'Management Service', 'IT', 'High');
