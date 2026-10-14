-- Address book data for use in various tests.
PRAGMA user_version = 1;

CREATE TABLE cards (uid TEXT PRIMARY KEY, localId INTEGER);
CREATE TABLE properties (card TEXT, name TEXT, value TEXT);
CREATE TABLE lists (uid TEXT PRIMARY KEY, localId INTEGER, name TEXT, nickName TEXT, description TEXT);
CREATE TABLE list_cards (list TEXT, card TEXT, PRIMARY KEY(list, card));

INSERT INTO cards (uid, localId) VALUES
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 1),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 2),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 3),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 4),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 5);

INSERT INTO properties (card, name, value) VALUES
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'FirstName', 'firs'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'LastName', 'lastn'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'PrimaryEmail', 'ema@test.invalid'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'LowercasePrimaryEmail', 'ema@test.invalid'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'DisplayName', 'd'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'NickName', 'ni'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'PreferMailFormat', '0'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'PopularityIndex', '0'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'AllowRemoteContent', '0'),
  ('9c4232ec-8992-44b2-8fd7-71dfb23a93c6', 'LastModifiedDate', '0'),

  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'FirstName', 'first'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'NickName', 'nic'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'PrimaryEmail', 'emai@test.invalid'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'LowercasePrimaryEmail', 'emai@test.invalid'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'LastName', 'l'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'DisplayName', 'di'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'PreferMailFormat', '0'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'PopularityIndex', '0'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'AllowRemoteContent', '0'),
  ('40326ec9-5361-4f8c-9797-0de3b28edce9', 'LastModifiedDate', '0'),

  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'DisplayName', 'dis'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'NickName', 'nick'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'PrimaryEmail', 'email@test.invalid'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'LowercasePrimaryEmail', 'email@test.invalid'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'FirstName', 'f'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'LastName', 'la'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'PreferMailFormat', '0'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'PopularityIndex', '0'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'AllowRemoteContent', '0'),
  ('f96f5eb1-6181-4588-b0d4-0fc47c9ac995', 'LastModifiedDate', '0'),

  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'LastName', 'las'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'DisplayName', 'disp'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'NickName', 'nickn'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'PrimaryEmail', 'e@test.invalid'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'LowercasePrimaryEmail', 'e@test.invalid'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'FirstName', 'fi'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'PreferMailFormat', '0'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'PopularityIndex', '0'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'AllowRemoteContent', '0'),
  ('a95c192c-ad3d-4e56-a7e3-8b969c80c717', 'LastModifiedDate', '0'),

  ('620c1226-eb2d-4df7-a532-f731544525ba', 'FirstName', 'fir'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'LastName', 'last'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'DisplayName', 'displ'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'PrimaryEmail', 'em@test.invalid'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'LowercasePrimaryEmail', 'em@test.invalid'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'NickName', 'n'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'PreferMailFormat', '0'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'PopularityIndex', 'a'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'AllowRemoteContent', '0'),
  ('620c1226-eb2d-4df7-a532-f731544525ba', 'LastModifiedDate', '0');

INSERT INTO lists (uid, localId, name, nickName, description) VALUES
  ('ab831252-d358-435b-a5a4-7f8536ea53d5', 6, 't', '', 'list'),
  ('52924d31-3a7d-420f-b4b4-039e9888ed08', 7, 'te', '', 'lis'),
  ('71b6f54e-dbc4-4bf0-a7d7-7235a5551ba5', 8, 'tes', '', 'li'),
  ('a0f4d368-7451-4756-b003-1018f231c7b4', 9, 'test', 'abcdef', 'l');
