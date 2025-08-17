# 17637437 - Level-Check

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 40 bytes          |
| Total Events     | 2                 |
| References Count | 1                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [119](#event-119)     | 0x0001       |     10 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |

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

### Event 119

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    71 10 00 80 71 11 01  10 21 00                  q...q...!.     
```

#### Opcodes

```
  0: 0x0001 [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
  1: 0x0005 [0x71] USER_INPUT_HANDLER: Process numerical input A (work=Work_Zone[1])
  2: 0x0009 [0x21] END_EVENT
  3: 0x000A [0x00] END_REQSTACK()
```
