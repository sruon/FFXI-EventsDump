# 17637627 - Mongra-Tester

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 72 bytes          |
| Total Events     | 2                 |
| References Count | 2                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [183](#event-183)     | 0x0001       |     38 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 183

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 38 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    02 00 80 00 80 00 25  00 71 10 00 80 71 11 02   ......%.q...q..
0010: 10 02 02 10 01 80 00 1E  00 21 00 01 22 00 B6 00  .........!.."...
0020: 02 10 01 01 00 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x0001 [0x02] IF !(1* == 1*) GOTO 0x0025
  1: 0x0009 [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
  2: 0x000D [0x71] USER_INPUT_HANDLER: Process numerical input A (work=Work_Zone[2])
  3: 0x0011 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x001E
  4: 0x0019 [0x21] END_EVENT
  5: 0x001A [0x00] END_REQSTACK()

SUBROUTINE_0022:
  6: 0x0022 [0x01] GOTO 0x0001
  7: 0x0025 [0x21] END_EVENT
  8: 0x0026 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x001B [0x01] GOTO 0x0022
```
