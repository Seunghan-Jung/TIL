# SQLite

## 닷 커맨드

### .help

사용가능한 닷 커맨드 명령어리스트를 보여준다.

```shell
.archive ...             Manage SQL archives
.auth ON|OFF             Show authorizer callbacks
.backup ?DB? FILE        Backup DB (default "main") to FILE
.bail on|off             Stop after hitting an error.  Default OFF
.binary on|off           Turn binary output on or off.  Default OFF
.cd DIRECTORY            Change the working directory to DIRECTORY
.changes on|off          Show number of rows changed by SQL
.check GLOB              Fail if output since .testcase does not match
.clone NEWDB             Clone data into NEWDB from the existing database
.databases               List names and files of attached databases
.dbconfig ?op? ?val?     List or change sqlite3_db_config() options
.dbinfo ?DB?             Show status information about the database
.dump ?TABLE?            Render database content as SQL
.echo on|off             Turn command echo on or off
.eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN
.excel                   Display the output of next command in spreadsheet
.exit ?CODE?             Exit this program with return-code CODE
.expert                  EXPERIMENTAL. Suggest indexes for queries
.explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto
.filectrl CMD ...        Run various sqlite3_file_control() operations
.fullschema ?--indent?   Show schema and the content of sqlite_stat tables
.headers on|off          Turn display of headers on or off
.help ?-all? ?PATTERN?   Show help text for PATTERN
.import FILE TABLE       Import data from FILE into TABLE
.imposter INDEX TABLE    Create imposter table TABLE on index INDEX
.indexes ?TABLE?         Show names of indexes
.limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT
.lint OPTIONS            Report potential schema issues.
.load FILE ?ENTRY?       Load an extension library
.log FILE|off            Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?       Set output mode
.nullvalue STRING        Use STRING in place of NULL values
.once ?OPTIONS? ?FILE?   Output for the next SQL command only to FILE
.open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
.output ?FILE?           Send output to FILE or stdout if FILE is omitted
.parameter CMD ...       Manage SQL parameter bindings
.print STRING...         Print literal STRING
.progress N              Invoke progress handler after every N opcodes
.prompt MAIN CONTINUE    Replace the standard prompts
.quit                    Exit this program
.read FILE               Read input from FILE
.recover                 Recover as much data as possible from corrupt db.
.restore ?DB? FILE       Restore content of DB (default "main") from FILE
.save FILE               Write in-memory database into FILE
.scanstats on|off        Turn sqlite3_stmt_scanstatus() metrics on or off
.schema ?PATTERN?        Show the CREATE statements matching PATTERN
.selftest ?OPTIONS?      Run tests defined in the SELFTEST table
.separator COL ?ROW?     Change the column and row separators
.sha3sum ...             Compute a SHA3 hash of database content
.shell CMD ARGS...       Run CMD ARGS... in a system shell
.show                    Show the current values for various settings
.stats ?on|off?          Show stats or turn stats on or off
.system CMD ARGS...      Run CMD ARGS... in a system shell
.tables ?TABLE?          List names of tables matching LIKE pattern TABLE
.testcase NAME           Begin redirecting output to 'testcase-out.txt'
.testctrl CMD ...        Run various sqlite3_test_control() operations
.timeout MS              Try opening locked tables for MS milliseconds
.timer on|off            Turn SQL timer on or off
.trace ?OPTIONS?         Output each SQL statement as it is run
.vfsinfo ?AUX?           Information about the top-level VFS
.vfslist                 List all available VFSes
.vfsname ?AUX?           Print the name of the VFS stack
.width NUM1 NUM2 ...     Set minimum column widths for columnar output
```

### .mode

`.mode MODE ?TABLE?`

테이블을 출력할 모드를 설정

- ascii
- box 
- column 
- csv 
- html 
- insert 
- json 
- line 
- list 
- markdown 
- quote 
- table 
- tabs 
- tcl

## 데이터 타입

| 표현                                                         | 결과    |
| ------------------------------------------------------------ | ------- |
| - INT<br />- INTEGER <br />- TINYINT<br />- SMALLINT<br />- MEDIUMINT<br />- BIGINT | INTEGER |
|                                                              |         |
|                                                              | TEXT    |
|                                                              | BLOB    |
|                                                              | REAL    |
|                                                              | NUMERIC |



## rowid

sqlite에서 테이블의 pk를 지정해주지 않으면 자동으로 생성된다

```sql
CREATE TABLE students(
  grade INTEGER,
  class INTEGER,
  name CHARACTER
);
```

위 처럼 pk로 설정한 컬럼이 없다면 자동으로 `rowid`라는 컬럼을 만드는데 이는 일반적으로  `select`문에서 보이지 않는다.

```sql
SELECT * FROM students
```

```
+-------+-------+------+
| grade | class | name |
+-------+-------+------+
| 1     | 1     | 정승한  |
| 2     | 1     | 이현도  |
| 4     | 1     | 김우주  |
| 5     | 5     | 미저리  |
| 6     | 6     | 참도현  |
| 3     | 3     | 정미라  |
+-------+-------+------+
```

조회할 컬럼에 `rowid`를 명시해주어야 조회할 수 있다.

```sql
SELECT rowid, * FROM students;
```

```text
+-------+-------+-------+------+
| rowid | grade | class | name |
+-------+-------+-------+------+
| 1     | 1     | 1     | 정승한  |
| 2     | 2     | 1     | 이현도  |
| 3     | 3     | 3     | 정미라  |
+-------+-------+-------+------+
```

- pk를 지정하더라도 rowid가 없는 것은 아니다.

  - 지정한 pk가 INTEGER라면 rowid는 그 pk와 동일한 값을 갖는다.

    ```sql
    CREATE TABLE students(
      id INTEGER PRIMARY KEY,
      grade INTEGER,
      class INTEGER,
      name CHARACTER
    );
    ```

    ```sql
    SELECT rowid, * FROM students;
    ```

    ```
    +----+----+-------+-------+------+
    | id | id | grade | class | name |
    +----+----+-------+-------+------+
    | 1  | 1  | 1     | 1     | 정승한  |
    | 2  | 2  | 2     | 1     | 이현도  |
    | 4  | 4  | 4     | 1     | 김우주  |
    | 5  | 5  | 5     | 5     | 미저리  |
    | 6  | 6  | 6     | 6     | 참도현  |
    | 7  | 7  | 3     | 3     | 정미라  |
    +----+----+-------+-------+------+
    ```

    rowid를 조회했지만 pk로 지정한 id 컬럼과 동일하게 나온다. 심지어 컬럼 이름도 id라고 나온다.  
    아마도 rowid가 id컬럼을 참조하는 것이거나 id 컬럼의 별칭으로 rowid가 생겨났다고 볼 수 있을 것 같다.

  - 지정한 pk가 INTEGER가 아니라면 rowid는 따로 존재한다.

- `rowid`는 다른 데이터베이스와 호환을 위해 `_rowid_`, `oid`라는 별칭을 가지고 있다.

- `rowid`는 기본적으로 `AUTOINCREMENT`가 아니다. 튜플이 추가 될 떄 현재 컬럼에 있는 값 중 최대값의 +1을 할당한다.  
  이와 달리 `AUTOINCREMENT`는 **현재까지** 할당 된 값 중 최대 값의 +1이 할당된다.

  ```sql
  +----+-------+-------+------+
  | id | grade | class | name |
  +----+-------+-------+------+
  | 1  | 1     | 1     | 정승한  |
  | 2  | 2     | 1     | 이현도  |
  | 3  | 3     | 3     | 정미라  |
  | 4  | 4     | 1     | 김우주  |
  | 5  | 5     | 5     | 미저리  |
  | 6  | 6     | 6     | 참도현  |
  +----+-------+-------+------+
  ```

  위 상황에서 마지막 행 (6, 6, 6, 참도현)을 지웠다 추가하면 다음과 같다.

  - `AUTOINCREMENT` O

    ```
    +-------+-------+-------+------+
    | rowid | grade | class | name |
    +-------+-------+-------+------+
    | 1     | 1     | 1     | 정승한  |
    | 2     | 2     | 1     | 이현도  |
    | 3     | 3     | 3     | 정미라  |
    | 4     | 4     | 1     | 김우주  |
    | 5     | 5     | 5     | 미저리  |
    | 7     | 6     | 6     | 참도현  |
    +-------+-------+-------+------+
    ```

  - `AUTOINCREMENT` X

    ```
    +-------+-------+-------+------+
    | rowid | grade | class | name |
    +-------+-------+-------+------+
    | 1     | 1     | 1     | 정승한  |
    | 2     | 2     | 1     | 이현도  |
    | 3     | 3     | 3     | 정미라  |
    | 4     | 4     | 1     | 김우주  |
    | 5     | 5     | 5     | 미저리  |
    | 6     | 6     | 6     | 참도현  |
    +-------+-------+-------+------+
    ```

    

