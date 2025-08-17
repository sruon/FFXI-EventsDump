# 17805336 - Young Aldo

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Hall of the Gods (ID: 251) |
| Block Size       | 412 bytes                  |
| Total Events     | 20                         |
| References Count | 7                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [5](#event-5)              | 0x0001       |      4 |              2 |
| [65535.1](#event-655351)   | 0x0005       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0015       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0025       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0035       |     16 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0055       |     16 |              2 |
| [65535.7](#event-655357)   | 0x0065       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0075       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0085       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0095       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00A5       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00B5       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00C5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00D5       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00E5       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00F5       |     16 |              2 |
| [65535.17](#event-6553517) | 0x0105       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0115       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0A0E      |        2574 |
|       2 | 0x0A0A      |        2570 |
|       3 | 0x0A0C      |        2572 |
|       4 | 0x0A0B      |        2571 |
|       5 | 0x0A0D      |        2573 |
|       6 | 0x0032      |          50 |

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

### Event 5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    C0 00 80 00                                     ....           
```

#### Opcodes

```
  0: 0x0001 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                5B 01 80  18 B0 0F 01 18 B0 0F 01       [..........
0010: 63 68 61 30 00                                    cha0.           
```

#### Opcodes

```
  0: 0x0005 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "cha0" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2574*
  1: 0x0014 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0015   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                5B 01 80  18 B0 0F 01 18 B0 0F 01       [..........
0020: 63 68 61 32 00                                    cha2.           
```

#### Opcodes

```
  0: 0x0015 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "cha2" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2574*
  1: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                5B 02 80  18 B0 0F 01 18 B0 0F 01       [..........
0030: 75 64 62 30 00                                    udb0.           
```

#### Opcodes

```
  0: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "udb0" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2570*
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                5B 01 80  18 B0 0F 01 18 B0 0F 01       [..........
0040: 68 79 6F 32 00                                    hyo2.           
```

#### Opcodes

```
  0: 0x0035 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hyo2" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2574*
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5B 03 80  18 B0 0F 01 18 B0 0F 01       [..........
0050: 75 6B 65 31 00                                    uke1.           
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "uke1" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2572*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                5B 03 80  18 B0 0F 01 18 B0 0F 01       [..........
0060: 75 6B 65 32 00                                    uke2.           
```

#### Opcodes

```
  0: 0x0055 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "uke2" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2572*
  1: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                5B 02 80  18 B0 0F 01 18 B0 0F 01       [..........
0070: 75 64 62 31 00                                    udb1.           
```

#### Opcodes

```
  0: 0x0065 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "udb1" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2570*
  1: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                5B 02 80  18 B0 0F 01 18 B0 0F 01       [..........
0080: 74 6C 63 30 00                                    tlc0.           
```

#### Opcodes

```
  0: 0x0075 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2570*
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                5B 02 80  18 B0 0F 01 18 B0 0F 01       [..........
0090: 74 6C 63 32 00                                    tlc2.           
```

#### Opcodes

```
  0: 0x0085 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc2" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2570*
  1: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                5B 02 80  18 B0 0F 01 18 B0 0F 01       [..........
00A0: 74 6C 63 33 00                                    tlc3.           
```

#### Opcodes

```
  0: 0x0095 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc3" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2570*
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                5B 04 80  18 B0 0F 01 18 B0 0F 01       [..........
00B0: 79 62 69 30 00                                    ybi0.           
```

#### Opcodes

```
  0: 0x00A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ybi0" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2571*
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                5B 04 80  18 B0 0F 01 18 B0 0F 01       [..........
00C0: 79 62 69 31 00                                    ybi1.           
```

#### Opcodes

```
  0: 0x00B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ybi1" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2571*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5B 05 80  18 B0 0F 01 18 B0 0F 01       [..........
00D0: 66 72 69 30 00                                    fri0.           
```

#### Opcodes

```
  0: 0x00C5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fri0" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2573*
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                5B 05 80  18 B0 0F 01 18 B0 0F 01       [..........
00E0: 66 72 69 31 00                                    fri1.           
```

#### Opcodes

```
  0: 0x00D5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fri1" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2573*
  1: 0x00E4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                5B 05 80  18 B0 0F 01 18 B0 0F 01       [..........
00F0: 66 72 69 32 00                                    fri2.           
```

#### Opcodes

```
  0: 0x00E5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fri2" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2573*
  1: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                5B 05 80  18 B0 0F 01 18 B0 0F 01       [..........
0100: 66 72 69 33 00                                    fri3.           
```

#### Opcodes

```
  0: 0x00F5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fri3" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2573*
  1: 0x0104 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0105   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                5B 05 80  18 B0 0F 01 18 B0 0F 01       [..........
0110: 66 72 69 34 00                                    fri4.           
```

#### Opcodes

```
  0: 0x0105 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fri4" with entities [Young Aldo (ID: 17805336/0x010FB018), Young Aldo (ID: 17805336/0x010FB018)], work=2573*
  1: 0x0114 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0115   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                6C F8 FF  FF 7F 06 80 00 80 00          l......... 
```

#### Opcodes

```
  0: 0x0115 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=50*, fade_time=1*)
  1: 0x011E [0x00] END_REQSTACK()
```
