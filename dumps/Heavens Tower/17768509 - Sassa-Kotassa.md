# 17768509 - Sassa-Kotassa

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 664 bytes               |
| Total Events     | 37                      |
| References Count | 7                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |      9 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     22 |              4 |
| [65535.4](#event-655354)   | 0x0030       |     16 |              2 |
| [65535.5](#event-655355)   | 0x0040       |     14 |              2 |
| [65535.6](#event-655356)   | 0x004E       |     16 |              2 |
| [65535.7](#event-655357)   | 0x005E       |     14 |              2 |
| [65535.8](#event-655358)   | 0x006C       |     16 |              2 |
| [65535.9](#event-655359)   | 0x007C       |     14 |              2 |
| [65535.10](#event-6553510) | 0x008A       |     16 |              2 |
| [65535.11](#event-6553511) | 0x009A       |     14 |              2 |
| [65535.12](#event-6553512) | 0x00A8       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00B8       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00C6       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00D6       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00E4       |     16 |              2 |
| [65535.17](#event-6553517) | 0x00F4       |     14 |              2 |
| [65535.18](#event-6553518) | 0x0102       |     16 |              2 |
| [65535.19](#event-6553519) | 0x0112       |     14 |              2 |
| [65535.20](#event-6553520) | 0x0120       |     16 |              2 |
| [65535.21](#event-6553521) | 0x0130       |     14 |              2 |
| [65535.22](#event-6553522) | 0x013E       |     16 |              2 |
| [65535.23](#event-6553523) | 0x014E       |     14 |              2 |
| [65535.24](#event-6553524) | 0x015C       |     16 |              2 |
| [65535.25](#event-6553525) | 0x016C       |     14 |              2 |
| [65535.26](#event-6553526) | 0x017A       |     16 |              2 |
| [65535.27](#event-6553527) | 0x018A       |     14 |              2 |
| [65535.28](#event-6553528) | 0x0198       |     16 |              2 |
| [65535.29](#event-6553529) | 0x01A8       |     22 |              4 |
| [53](#event-53)            | 0x01BE       |     19 |             10 |
| [442](#event-442)          | 0x01D1       |      1 |              1 |
| [445](#event-445)          | 0x01D2       |      1 |              1 |
| [451](#event-451)          | 0x01D3       |      1 |              1 |
| [457](#event-457)          | 0x01D4       |      1 |              1 |
| [455](#event-455)          | 0x01D5       |      1 |              1 |
| [462](#event-462)          | 0x01D6       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x01B0      |         432 |
|       3 | 0x002A      |          42 |
|       4 | 0x0029      |          41 |
|       5 | 0x0015      |          21 |
|       6 | 0x0016      |          22 |

## String References

- **21**: Adventurers from foreign countries are allowed access to the basement and first floor of Heavens Tower.
- **22**: The Star Sibyl believes that the Great Star Tree is not only the property of Windurst, but the property of all beings in Vana'diel.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                53 F8 FF FF 7F F8            S.....
0020: FF FF 7F 74 6C 6B 30 5E  69 64 6C 30 1C 01 80 00  ...tlk0^idl0....
```

#### Opcodes

```
  0: 0x001A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x002C [0x1C] WAIT(30* ticks)
  3: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 66 00 80 F8 FF FF 7F F8  FF FF 7F 64 69 73 30 00  f..........dis0.
```

#### Opcodes

```
  0: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 53 F8 FF FF 7F F8 FF FF  7F 64 69 73 30 00        S........dis0.  
```

#### Opcodes

```
  0: 0x0040 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            66 00                f.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        .........thk1.  
```

#### Opcodes

```
  0: 0x004E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            53 F8                S.
0060: FF FF 7F F8 FF FF 7F 74  68 6B 31 00              .......thk1.    
```

#### Opcodes

```
  0: 0x005E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      66 00 80 F8              f...
0070: FF FF 7F F8 FF FF 7F 74  68 6B 32 00              .......thk2.    
```

#### Opcodes

```
  0: 0x006C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      53 F8 FF FF              S...
0080: 7F F8 FF FF 7F 74 68 6B  32 00                    .....thk2.      
```

#### Opcodes

```
  0: 0x007C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                66 00 80 F8 FF FF            f.....
0090: 7F F8 FF FF 7F 73 79 75  30 00                    .....syu0.      
```

#### Opcodes

```
  0: 0x008A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "syu0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                53 F8 FF FF 7F F8            S.....
00A0: FF FF 7F 73 79 75 30 00                           ...syu0.        
```

#### Opcodes

```
  0: 0x009A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "syu0" with entities [EventEntity, EventEntity]
  1: 0x00A7 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A8   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                          66 00 80 F8 FF FF 7F F8          f.......
00B0: FF FF 7F 69 72 6F 30 00                           ...iro0.        
```

#### Opcodes

```
  0: 0x00A8 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00B7 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B8   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          53 F8 FF FF 7F F8 FF FF          S.......
00C0: 7F 69 72 6F 30 00                                 .iro0.          
```

#### Opcodes

```
  0: 0x00B8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   66 00  80 F8 FF FF 7F F8 FF FF        f.........
00D0: 7F 70 6F 69 30 00                                 .poi0.          
```

#### Opcodes

```
  0: 0x00C6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   53 F8  FF FF 7F F8 FF FF 7F 65        S........e
00E0: 68 6E 30 00                                       hn0.            
```

#### Opcodes

```
  0: 0x00D6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn0" with entities [EventEntity, EventEntity]
  1: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             5B 02 80 F8  FF FF 7F F8 FF FF 7F 79      [..........y
00F0: 65 73 30 00                                       es0.            
```

#### Opcodes

```
  0: 0x00E4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "yes0" with entities [EventEntity, EventEntity], work=432*
  1: 0x00F3 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F4   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             53 F8 FF FF  7F F8 FF FF 7F 79 65 73      S........yes
0100: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00F4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "yes0" with entities [EventEntity, EventEntity]
  1: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       66 00 80 F8 FF FF  7F F8 FF FF 7F 6F 62 69    f..........obi
0110: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0102 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "obi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0111 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0112   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       53 F8 FF FF 7F F8  FF FF 7F 6F 62 69 30 00    S........obi0.
```

#### Opcodes

```
  0: 0x0112 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "obi0" with entities [EventEntity, EventEntity]
  1: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 66 00 80 F8 FF FF 7F F8  FF FF 7F 6F 62 69 31 00  f..........obi1.
```

#### Opcodes

```
  0: 0x0120 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "obi1" with entities [EventEntity, EventEntity], work=40*
  1: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 53 F8 FF FF 7F F8 FF FF  7F 6F 62 69 31 00        S........obi1.  
```

#### Opcodes

```
  0: 0x0130 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "obi1" with entities [EventEntity, EventEntity]
  1: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            66 03                f.
0140: 80 F8 FF FF 7F F8 FF FF  7F 62 69 6B 30 00        .........bik0.  
```

#### Opcodes

```
  0: 0x013E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
  1: 0x014D [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                            53 F8                S.
0150: FF FF 7F F8 FF FF 7F 62  69 6B 30 00              .......bik0.    
```

#### Opcodes

```
  0: 0x014E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x015B [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                      66 03 80 F8              f...
0160: FF FF 7F F8 FF FF 7F 62  69 6B 31 00              .......bik1.    
```

#### Opcodes

```
  0: 0x015C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik1" with entities [EventEntity, EventEntity], work=42*
  1: 0x016B [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                      53 F8 FF FF              S...
0170: 7F F8 FF FF 7F 62 69 6B  31 00                    .....bik1.      
```

#### Opcodes

```
  0: 0x016C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik1" with entities [EventEntity, EventEntity]
  1: 0x0179 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                66 04 80 F8 FF FF            f.....
0180: 7F F8 FF FF 7F 73 68 6B  30 00                    .....shk0.      
```

#### Opcodes

```
  0: 0x017A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
  1: 0x0189 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                53 F8 FF FF 7F F8            S.....
0190: FF FF 7F 73 68 6B 30 00                           ...shk0.        
```

#### Opcodes

```
  0: 0x018A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [EventEntity, EventEntity]
  1: 0x0197 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0198   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          66 00 80 F8 FF FF 7F F8          f.......
01A0: FF FF 7F 7A 69 74 30 00                           ...zit0.        
```

#### Opcodes

```
  0: 0x0198 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "zit0" with entities [EventEntity, EventEntity], work=40*
  1: 0x01A7 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A8   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                          53 F8 FF FF 7F F8 FF FF          S.......
01B0: 7F 7A 69 74 30 5E 69 64  6C 30 1C 01 80 00        .zit0^idl0....  
```

#### Opcodes

```
  0: 0x01A8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "zit0" with entities [EventEntity, EventEntity]
  1: 0x01B5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x01BA [0x1C] WAIT(30* ticks)
  3: 0x01BD [0x00] END_REQSTACK()
```

### Event 53

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01BE   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                                            1E F0                ..
01C0: FF FF 7F 6F 70 1D 05 80  23 1D 06 80 23 20 00 21  ...op...#...# .!
01D0: 00                                                .               
```

#### Opcodes

```
  0: 0x01BE [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01C3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x01C4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x01C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=21*)
    → "Adventurers from foreign countries are allowed access to the basement and first floor of Heavens Tower."
  4: 0x01C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x01C9 [0x1D] PRINT_EVENT_MESSAGE(message_id=22*)
    → "The Star Sibyl believes that the Great Star Tree is not only the property of Windurst, but the property of all beings in Vana'diel."
  6: 0x01CC [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01CD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x01CF [0x21] END_EVENT
  9: 0x01D0 [0x00] END_REQSTACK()
```

### Event 442

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:    00                                              .              
```

#### Opcodes

```
  0: 0x01D1 [0x00] END_REQSTACK()
```

### Event 445

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:       00                                            .             
```

#### Opcodes

```
  0: 0x01D2 [0x00] END_REQSTACK()
```

### Event 451

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:          00                                          .            
```

#### Opcodes

```
  0: 0x01D3 [0x00] END_REQSTACK()
```

### Event 457

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:             00                                        .           
```

#### Opcodes

```
  0: 0x01D4 [0x00] END_REQSTACK()
```

### Event 455

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                00                                      .          
```

#### Opcodes

```
  0: 0x01D5 [0x00] END_REQSTACK()
```

### Event 462

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01D6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                   00                                    .         
```

#### Opcodes

```
  0: 0x01D6 [0x00] END_REQSTACK()
```
