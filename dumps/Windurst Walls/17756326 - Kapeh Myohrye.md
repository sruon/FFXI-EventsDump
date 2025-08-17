# 17756326 - Kapeh Myohrye

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 324 bytes                |
| Total Events     | 13                       |
| References Count | 18                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     29 |              3 |
| [65535.6](#event-655356)   | 0x005A       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0068       |     24 |              4 |
| [473](#event-473)          | 0x0080       |      7 |              2 |
| [65535.8](#event-655358)   | 0x0087       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0091       |     19 |              5 |
| [65535.10](#event-6553510) | 0x00A4       |     10 |              2 |
| [65535.11](#event-6553511) | 0x00AE       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01FB      |         507 |
|       1 | 0x002A      |          42 |
|       2 | 0x001E      |          30 |
|       3 | 0xFFFE8E1E  |  4294872606 |
|       4 | 0x2EE01     |      192001 |
|       5 | 0xFFFFCD38  |  4294954296 |
|       6 | 0x09E9      |        2537 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFFE7ADC  |  4294867676 |
|       9 | 0x303DE     |      197598 |
|      10 | 0xFFFFD120  |  4294955296 |
|      11 | 0xFFFE7F34  |  4294868788 |
|      12 | 0x319AF     |      203183 |
|      13 | 0x05FF      |        1535 |
|      14 | 0xFFFE7C7D  |  4294868093 |
|      15 | 0x315D7     |      202199 |
|      16 | 0xFFFFD121  |  4294955297 |
|      17 | 0x067E      |        1662 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 79 6D 69 30   [..........ymi0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ymi0" with entities [EventEntity, EventEntity], work=507*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 79 6D 69 30 00      S........ymi0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ymi0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 79 6D 69 31 00     ..........ymi1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ymi1" with entities [EventEntity, EventEntity], work=507*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  79 6D 69 31 00           ........ymi1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ymi1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         66 01 80               f..
0040: F8 FF FF 7F F8 FF FF 7F  77 6F 6E 32 2C F8 FF FF  ........won2,...
0050: 7F F8 FF FF 7F 6C 63 30  36 00                    .....lc06.      
```

#### Opcodes

```
  0: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "won2" with entities [EventEntity, EventEntity], work=42*
  1: 0x004C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "lc06" with entities [EventEntity, EventEntity]
  2: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                53 F8 FF FF 7F F8            S.....
0060: FF FF 7F 6C 63 30 36 00                           ...lc06.        
```

#### Opcodes

```
  0: 0x005A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "lc06" with entities [EventEntity, EventEntity]
  1: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          66 01 80 F8 FF FF 7F F8          f.......
0070: FF FF 7F 77 6F 66 32 5E  69 64 6C 30 1C 02 80 00  ...wof2^idl0....
```

#### Opcodes

```
  0: 0x0068 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wof2" with entities [EventEntity, EventEntity], work=42*
  1: 0x0077 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x007C [0x1C] WAIT(30* ticks)
  3: 0x007F [0x00] END_REQSTACK()
```

### Event 473

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0080 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      37  03 80 04 80 05 80 06 80         7........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0087 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-94.690*, z=192.001*, y=-13.000*, direction=223.0°*
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    32 07 80 5A 00 08 80  09 80 0A 80 5A 01 1E 9E   2..Z.......Z...
00A0: F0 0E 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0091 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0094 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-99.620*, Z=197.598*, Y=-12.000*
  2: 0x009C [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x009E [0x1E] EventEntity looks at ??? (ID: 17756318/0x010EF09E) and starts talking
  4: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             37 0B 80 0C  80 0A 80 0D 80 00            7.........  
```

#### Opcodes

```
  0: 0x00A4 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-98.508*, z=203.183*, y=-12.000*, direction=134.9°*
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            37 0E                7.
00B0: 80 0F 80 10 80 11 80 00                           ........        
```

#### Opcodes

```
  0: 0x00AE [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-99.203*, z=202.199*, y=-11.999*, direction=146.1°*
  1: 0x00B7 [0x00] END_REQSTACK()
```
