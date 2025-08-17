# 17563917 - Shantotto

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Inner Horutoto Ruins (ID: 192) |
| Block Size       | 672 bytes                      |
| Total Events     | 30                             |
| References Count | 19                             |

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
| [65535.7](#event-655357)   | 0x0063       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0073       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0081       |     16 |              2 |
| [65535.10](#event-6553510) | 0x0091       |     22 |              4 |
| [65535.11](#event-6553511) | 0x00A7       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00B7       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00C5       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00D5       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00E3       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00F3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x0101       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0111       |     14 |              2 |
| [65535.19](#event-6553519) | 0x011F       |     16 |              2 |
| [65535.20](#event-6553520) | 0x012F       |     22 |              4 |
| [65535.21](#event-6553521) | 0x0145       |     16 |              2 |
| [65535.22](#event-6553522) | 0x0155       |     22 |              4 |
| [65535.23](#event-6553523) | 0x016B       |      9 |              3 |
| [73](#event-73)            | 0x0174       |      1 |              1 |
| [65535.24](#event-6553524) | 0x0175       |     10 |              2 |
| [65535.25](#event-6553525) | 0x017F       |     27 |              7 |
| [65535.26](#event-6553526) | 0x019A       |     24 |              6 |
| [65535.27](#event-6553527) | 0x01B2       |     19 |              5 |
| [65535.28](#event-6553528) | 0x01C5       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x002A      |          42 |
|       4 | 0xFFFC81F2  |  4294738418 |
|       5 | 0x23061     |      143457 |
|       6 | 0x0000      |           0 |
|       7 | 0x0BFF      |        3071 |
|       8 | 0x000D      |          13 |
|       9 | 0xFFFC8105  |  4294738181 |
|      10 | 0x23DD2     |      146898 |
|      11 | 0x0EEA      |        3818 |
|      12 | 0xFFFC833D  |  4294738749 |
|      13 | 0x22EEE     |      143086 |
|      14 | 0xFFFC73EF  |  4294734831 |
|      15 | 0x229BB     |      141755 |
|      16 | 0xFFFFFFA7  |  4294967207 |
|      17 | 0x1CC7      |        7367 |
|      18 | 0x1CCE      |        7374 |

## String References

- **7367**: Yes. What i\`s this?
- **7374**: Well, I'm just about as disappointed as one could be. I thought we would be finding something goody.

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
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
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
0040:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 70 61     f..........pa
0070: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          53 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30     S........pas0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    66 02 80 F8 FF FF 7F  F8 FF FF 7F 6F 68 68 30   f..........ohh0
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0081 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=41*
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    53 F8 FF FF 7F F8 FF  FF 7F 6F 68 68 30 5E 69   S........ohh0^i
00A0: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0091 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ohh0" with entities [EventEntity, EventEntity]
  1: 0x009E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00A3 [0x1C] WAIT(30* ticks)
  3: 0x00A6 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A7   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      66  02 80 F8 FF FF 7F F8 FF         f........
00B0: FF 7F 73 68 6B 30 00                              ..shk0.         
```

#### Opcodes

```
  0: 0x00A7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "shk0" with entities [EventEntity, EventEntity], work=41*
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00C0: 73 68 6B 30 00                                    shk0.           
```

#### Opcodes

```
  0: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "shk0" with entities [EventEntity, EventEntity]
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
00C0:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
00D0: 64 69 73 30 00                                    dis0.           
```

#### Opcodes

```
  0: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00D4 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                53 F8 FF  FF 7F F8 FF FF 7F 64 69       S........di
00E0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x00E2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 70 6F     f..........po
00F0: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x00E3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00F2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          53 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30     S........poi0
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00F3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0101   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 69 72 6F 30   f..........iro0
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0101 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0110 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0111   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    53 F8 FF FF 7F F8 FF  FF 7F 69 72 6F 30 00      S........iro0. 
```

#### Opcodes

```
  0: 0x0111 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
  1: 0x011E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                               66                 f
0120: 02 80 F8 FF FF 7F F8 FF  FF 7F 65 68 6E 30 00     ..........ehn0. 
```

#### Opcodes

```
  0: 0x011F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn0" with entities [EventEntity, EventEntity], work=41*
  1: 0x012E [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012F   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                               53                 S
0130: F8 FF FF 7F F8 FF FF 7F  65 68 6E 30 5E 69 64 6C  ........ehn0^idl
0140: 30 1C 01 80 00                                    0....           
```

#### Opcodes

```
  0: 0x012F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn0" with entities [EventEntity, EventEntity]
  1: 0x013C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0141 [0x1C] WAIT(30* ticks)
  3: 0x0144 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0145   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                66 03 80  F8 FF FF 7F F8 FF FF 7F       f..........
0150: 62 69 6B 30 00                                    bik0.           
```

#### Opcodes

```
  0: 0x0145 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
  1: 0x0154 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0155   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                53 F8 FF  FF 7F F8 FF FF 7F 62 69       S........bi
0160: 6B 30 5E 69 64 6C 30 1C  01 80 00                 k0^idl0....     
```

#### Opcodes

```
  0: 0x0155 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x0162 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0167 [0x1C] WAIT(30* ticks)
  3: 0x016A [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x016B  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                   5E 69 64 6C 30             ^idl0
0170: 1C 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x016B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0170 [0x1C] WAIT(30* ticks)
  2: 0x0173 [0x00] END_REQSTACK()
```

### Event 73

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0174  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:             00                                        .           
```

#### Opcodes

```
  0: 0x0174 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0175   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                37 04 80  05 80 06 80 07 80 00          7......... 
```

#### Opcodes

```
  0: 0x0175 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-228.878*, z=143.457*, y=0.000*, direction=269.9°*
  1: 0x017E [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017F   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                               32                 2
0180: 08 80 1F 00 09 80 0A 80  06 80 1F 01 4B 0D 01 0C  ............K...
0190: 01 0B 80 6F 76 0D 01 0C  01 00                    ...ov.....      
```

#### Opcodes

```
  0: 0x017F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0182 [0x1F] MOVE_ENTITY: EventEntity moves to X=-229.115*, Z=146.898*, Y=0.000*
  2: 0x018A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x018C [0x4B] UPDATE_ENTITY_YAW(entity=Shantotto (ID: 17563917/0x010C010D), yaw=21.0°*)
  4: 0x0193 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0194 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Shantotto (ID: 17563917/0x010C010D) Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0199 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019A   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                32 08 80 1F 00 0C            2.....
01A0: 80 0D 80 06 80 1F 01 1F  00 0E 80 0F 80 10 80 1F  ................
01B0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x019A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x019D [0x1F] MOVE_ENTITY: EventEntity moves to X=-228.547*, Z=143.086*, Y=0.000*
  2: 0x01A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-232.465*, Z=141.755*, Y=-0.089*
  4: 0x01AF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x01B1 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B2   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:       29 08 0D 01 0C 01  01 1D 11 80 23 29 08 0D    ).........#)..
01C0: 01 0C 01 02 00                                    .....           
```

#### Opcodes

```
  0: 0x01B2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Shantotto (ID: 17563917/0x010C010D), tag_num=0x01)
  1: 0x01B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7367*)
    → "Yes. What i`s this?"
  2: 0x01BC [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01BD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Shantotto (ID: 17563917/0x010C010D), tag_num=0x02)
  4: 0x01C4 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01C5  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                1D 12 80  23 00                         ...#.      
```

#### Opcodes

```
  0: 0x01C5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7374*)
    → "Well, I'm just about as disappointed as one could be. I thought we would be finding something goody."
  1: 0x01C8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x01C9 [0x00] END_REQSTACK()
```
