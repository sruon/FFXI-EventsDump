# 17760349 - Kohlo-Lakolo

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 932 bytes               |
| Total Events     | 39                      |
| References Count | 11                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0055       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0063       |     57 |              5 |
| [65535.8](#event-655358)   | 0x009C       |     22 |              3 |
| [65535.9](#event-655359)   | 0x00B2       |     20 |              3 |
| [65535.10](#event-6553510) | 0x00C6       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00D6       |     22 |              4 |
| [65535.12](#event-6553512) | 0x00EC       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00FC       |     22 |              4 |
| [65535.14](#event-6553514) | 0x0112       |     22 |              3 |
| [65535.15](#event-6553515) | 0x0128       |     20 |              3 |
| [65535.16](#event-6553516) | 0x013C       |     22 |              3 |
| [65535.17](#event-6553517) | 0x0152       |     20 |              3 |
| [65535.18](#event-6553518) | 0x0166       |     22 |              3 |
| [65535.19](#event-6553519) | 0x017C       |     22 |              4 |
| [65535.20](#event-6553520) | 0x0192       |     16 |              2 |
| [65535.21](#event-6553521) | 0x01A2       |     14 |              2 |
| [65535.22](#event-6553522) | 0x01B0       |     16 |              2 |
| [65535.23](#event-6553523) | 0x01C0       |     22 |              4 |
| [65535.24](#event-6553524) | 0x01D6       |     16 |              2 |
| [65535.25](#event-6553525) | 0x01E6       |     14 |              2 |
| [65535.26](#event-6553526) | 0x01F4       |     22 |              3 |
| [65535.27](#event-6553527) | 0x020A       |     20 |              3 |
| [65535.28](#event-6553528) | 0x021E       |     16 |              2 |
| [65535.29](#event-6553529) | 0x022E       |     14 |              2 |
| [65535.30](#event-6553530) | 0x023C       |     16 |              2 |
| [65535.31](#event-6553531) | 0x024C       |     14 |              2 |
| [65535.32](#event-6553532) | 0x025A       |      9 |              3 |
| [65535.33](#event-6553533) | 0x0263       |     50 |              5 |
| [65535.34](#event-6553534) | 0x0295       |     16 |              2 |
| [65535.35](#event-6553535) | 0x02A5       |     14 |              2 |
| [584](#event-584)          | 0x02B3       |      1 |              1 |
| [65535.36](#event-6553536) | 0x02B4       |     10 |              2 |
| [65535.37](#event-6553537) | 0x02BE       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0x0058      |          88 |
|       3 | 0x0056      |          86 |
|       4 | 0xFFFFA67D  |  4294944381 |
|       5 | 0x2E6B5     |      190133 |
|       6 | 0xFFFFE890  |  4294961296 |
|       7 | 0x0013      |          19 |
|       8 | 0x0015      |          21 |
|       9 | 0xFFFFADC5  |  4294946245 |
|      10 | 0x2E71C     |      190236 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=85*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
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
0040:                5B 00 80  F8 FF FF 7F F8 FF FF 7F       [..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=85*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0060: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 57 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          5B 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68     [..........th
0070: 6B 31 53 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 5B  k1S........thk1[
0080: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 53 F8  ..........thk2S.
0090: FF FF 7F F8 FF FF 7F 74  68 6B 32 00              .......thk2.    
```

#### Opcodes

```
  0: 0x0063 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=85*
  1: 0x0072 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x007F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=85*
  3: 0x008E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  4: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      7C 00 F8 FF              |...
00A0: FF 7F 5B 00 80 F8 FF FF  7F F8 FF FF 7F 65 68 65  ..[..........ehe
00B0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x009C [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x00A2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ehe0" with entities [EventEntity, EventEntity], work=85*
  2: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 7C    S........tlk0|
00C0: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x00B2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x00BF [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
00D0: 7F 61 6E 67 30 00                                 .ang0.          
```

#### Opcodes

```
  0: 0x00C6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=85*
  1: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   53 F8  FF FF 7F F8 FF FF 7F 61        S........a
00E0: 6E 67 30 5E 69 64 6C 30  1C 01 80 00              ng0^idl0....    
```

#### Opcodes

```
  0: 0x00D6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x00E3 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00E8 [0x1C] WAIT(30* ticks)
  3: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      5B 00 80 F8              [...
00F0: FF FF 7F F8 FF FF 7F 6B  6F 77 30 00              .......kow0.    
```

#### Opcodes

```
  0: 0x00EC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kow0" with entities [EventEntity, EventEntity], work=85*
  1: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      53 F8 FF FF              S...
0100: 7F F8 FF FF 7F 6B 6F 77  30 5E 69 64 6C 30 1C 01  .....kow0^idl0..
0110: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00FC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kow0" with entities [EventEntity, EventEntity]
  1: 0x0109 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x010E [0x1C] WAIT(30* ticks)
  3: 0x0111 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0112   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       7C 00 F8 FF FF 7F  5B 00 80 F8 FF FF 7F F8    |.....[.......
0120: FF FF 7F 73 75 72 30 00                           ...sur0.        
```

#### Opcodes

```
  0: 0x0112 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0118 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sur0" with entities [EventEntity, EventEntity], work=85*
  2: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          53 F8 FF FF 7F F8 FF FF          S.......
0130: 7F 73 75 72 30 7C 01 F8  FF FF 7F 00              .sur0|......    
```

#### Opcodes

```
  0: 0x0128 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sur0" with entities [EventEntity, EventEntity]
  1: 0x0135 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x013B [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013C   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                      7C 00 F8 FF              |...
0140: FF 7F 5B 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..[..........tlk
0150: 32 00                                             2.              
```

#### Opcodes

```
  0: 0x013C [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0142 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=85*
  2: 0x0151 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0152   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:       53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 32 7C    S........tlk2|
0160: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0152 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  1: 0x015F [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x0165 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0166   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                   7C 01  F8 FF FF 7F 5B 00 80 F8        |.....[...
0170: FF FF 7F F8 FF FF 7F 6B  6F 75 30 00              .......kou0.    
```

#### Opcodes

```
  0: 0x0166 [0x7C] EventEntity->Render.Flags2 |= 0x01
  1: 0x016C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kou0" with entities [EventEntity, EventEntity], work=85*
  2: 0x017B [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017C   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                      53 F8 FF FF              S...
0180: 7F F8 FF FF 7F 6B 6F 75  30 5E 69 64 6C 30 1C 01  .....kou0^idl0..
0190: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x017C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kou0" with entities [EventEntity, EventEntity]
  1: 0x0189 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x018E [0x1C] WAIT(30* ticks)
  3: 0x0191 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0192   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:       5B 00 80 F8 FF FF  7F F8 FF FF 7F 6A 6D 70    [..........jmp
01A0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0192 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=85*
  1: 0x01A1 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:       53 F8 FF FF 7F F8  FF FF 7F 6A 6D 70 30 00    S........jmp0.
```

#### Opcodes

```
  0: 0x01A2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jmp0" with entities [EventEntity, EventEntity]
  1: 0x01AF [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 70 61 6E 30 00  [..........pan0.
```

#### Opcodes

```
  0: 0x01B0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pan0" with entities [EventEntity, EventEntity], work=85*
  1: 0x01BF [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C0   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 53 F8 FF FF 7F F8 FF FF  7F 70 61 6E 30 5E 69 64  S........pan0^id
01D0: 6C 30 1C 01 80 00                                 l0....          
```

#### Opcodes

```
  0: 0x01C0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pan0" with entities [EventEntity, EventEntity]
  1: 0x01CD [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x01D2 [0x1C] WAIT(30* ticks)
  3: 0x01D5 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
01E0: 7F 70 61 73 30 00                                 .pas0.          
```

#### Opcodes

```
  0: 0x01D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=85*
  1: 0x01E5 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E6   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                   53 F8  FF FF 7F F8 FF FF 7F 70        S........p
01F0: 61 73 30 00                                       as0.            
```

#### Opcodes

```
  0: 0x01E6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x01F3 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F4   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:             7C 00 F8 FF  FF 7F 5B 00 80 F8 FF FF      |.....[.....
0200: 7F F8 FF FF 7F 62 61 6E  30 00                    .....ban0.      
```

#### Opcodes

```
  0: 0x01F4 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x01FA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ban0" with entities [EventEntity, EventEntity], work=85*
  2: 0x0209 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x020A   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:                                53 F8 FF FF 7F F8            S.....
0210: FF FF 7F 62 61 6E 30 7C  01 F8 FF FF 7F 00        ...ban0|......  
```

#### Opcodes

```
  0: 0x020A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ban0" with entities [EventEntity, EventEntity]
  1: 0x0217 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x021D [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x021E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                                            5B 02                [.
0220: 80 F8 FF FF 7F F8 FF FF  7F 66 6B 72 30 00        .........fkr0.  
```

#### Opcodes

```
  0: 0x021E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fkr0" with entities [EventEntity, EventEntity], work=88*
  1: 0x022D [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x022E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                            53 F8                S.
0230: FF FF 7F F8 FF FF 7F 66  6B 72 30 00              .......fkr0.    
```

#### Opcodes

```
  0: 0x022E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fkr0" with entities [EventEntity, EventEntity]
  1: 0x023B [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x023C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                                      5B 02 80 F8              [...
0240: FF FF 7F F8 FF FF 7F 66  6B 72 31 00              .......fkr1.    
```

#### Opcodes

```
  0: 0x023C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fkr1" with entities [EventEntity, EventEntity], work=88*
  1: 0x024B [0x00] END_REQSTACK()
```

### Event 65535.31

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                      53 F8 FF FF              S...
0250: 7F F8 FF FF 7F 66 6B 72  31 00                    .....fkr1.      
```

#### Opcodes

```
  0: 0x024C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "fkr1" with entities [EventEntity, EventEntity]
  1: 0x0259 [0x00] END_REQSTACK()
```

### Event 65535.32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x025A  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0250:                                5E 69 64 6C 30 1C            ^idl0.
0260: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x025A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x025F [0x1C] WAIT(30* ticks)
  2: 0x0262 [0x00] END_REQSTACK()
```

### Event 65535.33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0263   |
| Data Size    | 50 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0260:          7C 00 F8 FF FF  7F 5B 00 80 F8 FF FF 7F     |.....[......
0270: F8 FF FF 7F 73 75 72 30  53 F8 FF FF 7F F8 FF FF  ....sur0S.......
0280: 7F 73 75 72 30 5B 00 80  F8 FF FF 7F F8 FF FF 7F  .sur0[..........
0290: 61 6E 67 30 00                                    ang0.           
```

#### Opcodes

```
  0: 0x0263 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0269 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sur0" with entities [EventEntity, EventEntity], work=85*
  2: 0x0278 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sur0" with entities [EventEntity, EventEntity]
  3: 0x0285 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=85*
  4: 0x0294 [0x00] END_REQSTACK()
```

### Event 65535.34

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0295   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:                5B 03 80  F8 FF FF 7F F8 FF FF 7F       [..........
02A0: 6F 72 62 30 00                                    orb0.           
```

#### Opcodes

```
  0: 0x0295 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "orb0" with entities [EventEntity, EventEntity], work=86*
  1: 0x02A4 [0x00] END_REQSTACK()
```

### Event 65535.35

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02A5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:                53 F8 FF  FF 7F F8 FF FF 7F 6F 72       S........or
02B0: 62 30 00                                          b0.             
```

#### Opcodes

```
  0: 0x02A5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "orb0" with entities [EventEntity, EventEntity]
  1: 0x02B2 [0x00] END_REQSTACK()
```

### Event 584

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x02B3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:          00                                          .            
```

#### Opcodes

```
  0: 0x02B3 [0x00] END_REQSTACK()
```

### Event 65535.36

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02B4   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:             37 04 80 05  80 06 80 07 80 00            7.........  
```

#### Opcodes

```
  0: 0x02B4 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-22.915*, z=190.133*, y=-6.000*, direction=1.7°*
  1: 0x02BD [0x00] END_REQSTACK()
```

### Event 65535.37

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02BE   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                            32 08                2.
02C0: 80 1F 00 09 80 0A 80 06  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x02BE [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x02C1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-21.051*, Z=190.236*, Y=-6.000*
  2: 0x02C9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x02CB [0x00] END_REQSTACK()
```
