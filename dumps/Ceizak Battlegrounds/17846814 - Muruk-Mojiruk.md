# 17846814 - Muruk-Mojiruk

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Ceizak Battlegrounds (ID: 261) |
| Block Size       | 668 bytes                      |
| Total Events     | 29                             |
| References Count | 24                             |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |      6 |              2 |
| [65535.4](#event-655354)   | 0x002D       |     16 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     14 |              2 |
| [65535.6](#event-655356)   | 0x004B       |     16 |              2 |
| [65535.7](#event-655357)   | 0x005B       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0069       |     16 |              2 |
| [65535.9](#event-655359)   | 0x0079       |     14 |              2 |
| [65535.10](#event-6553510) | 0x0087       |     16 |              2 |
| [65535.11](#event-6553511) | 0x0097       |     14 |              2 |
| [65535.12](#event-6553512) | 0x00A5       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00B5       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00C3       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00D3       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00E1       |     16 |              2 |
| [65535.17](#event-6553517) | 0x00F1       |     14 |              2 |
| [65535.18](#event-6553518) | 0x00FF       |     16 |              2 |
| [65535.19](#event-6553519) | 0x010F       |     14 |              2 |
| [65535.20](#event-6553520) | 0x011D       |     16 |              2 |
| [65535.21](#event-6553521) | 0x012D       |     14 |              2 |
| [502](#event-502)          | 0x013B       |     55 |             12 |
| [20](#event-20)            | 0x0172       |      1 |              1 |
| [65535.22](#event-6553522) | 0x0173       |     10 |              2 |
| [65535.23](#event-6553523) | 0x017D       |     10 |              2 |
| [65535.24](#event-6553524) | 0x0187       |     14 |              4 |
| [65535.25](#event-6553525) | 0x0195       |     21 |              7 |
| [65535.26](#event-6553526) | 0x01AA       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0029      |          41 |
|       3 | 0x1F6A      |        8042 |
|       4 | 0x0000      |           0 |
|       5 | 0x1F6B      |        8043 |
|       6 | 0x5A03C     |      368700 |
|       7 | 0x2BD9F     |      179615 |
|       8 | 0x0169      |         361 |
|       9 | 0x0CFE      |        3326 |
|      10 | 0x5B87C     |      374908 |
|      11 | 0x29920     |      170272 |
|      12 | 0x017C      |         380 |
|      13 | 0x06B0      |        1712 |
|      14 | 0x5B265     |      373349 |
|      15 | 0x2A7FF     |      174079 |
|      16 | 0x01FD      |         509 |
|      17 | 0x000D      |          13 |
|      18 | 0x5BAF0     |      375536 |
|      19 | 0x29214     |      168468 |
|      20 | 0x014D      |         333 |
|      21 | 0x5C3B8     |      377784 |
|      22 | 0x28FFE     |      167934 |
|      23 | 0x01B2      |         434 |

## String References

- **8042**: My heartaru goes out to all you pioneers. As if the dangers of the jungle weren't enough, you've also got to contend with the foul beasts within. It's a position I certainly do not envy-wenvy.
- **8043**: A warm smile and a pataru on the back is all I am able to provide, but Elmric at the south side of tent-went may be able to give you more.

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 00                  ^idl0.   
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         66 00 80               f..
0030: F8 FF FF 7F F8 FF FF 7F  70 6F 69 30 00           ........poi0.   
```

#### Opcodes

```
  0: 0x002D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         53 F8 FF               S..
0040: FF 7F F8 FF FF 7F 70 6F  69 30 00                 ......poi0.     
```

#### Opcodes

```
  0: 0x003D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   66 02 80 F8 FF             f....
0050: FF 7F F8 FF FF 7F 65 68  6E 30 00                 ......ehn0.     
```

#### Opcodes

```
  0: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn0" with entities [EventEntity, EventEntity], work=41*
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   53 F8 FF FF 7F             S....
0060: F8 FF FF 7F 65 68 6E 30  00                       ....ehn0.       
```

#### Opcodes

```
  0: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn0" with entities [EventEntity, EventEntity]
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             66 02 80 F8 FF FF 7F           f......
0070: F8 FF FF 7F 65 68 6E 31  00                       ....ehn1.       
```

#### Opcodes

```
  0: 0x0069 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ehn1" with entities [EventEntity, EventEntity], work=41*
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             53 F8 FF FF 7F F8 FF           S......
0080: FF 7F 65 68 6E 31 00                              ..ehn1.         
```

#### Opcodes

```
  0: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ehn1" with entities [EventEntity, EventEntity]
  1: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      66  00 80 F8 FF FF 7F F8 FF         f........
0090: FF 7F 7A 69 74 30 00                              ..zit0.         
```

#### Opcodes

```
  0: 0x0087 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "zit0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00A0: 7A 69 74 30 00                                    zit0.           
```

#### Opcodes

```
  0: 0x0097 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "zit0" with entities [EventEntity, EventEntity]
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
00B0: 77 61 69 30 00                                    wai0.           
```

#### Opcodes

```
  0: 0x00A5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wai0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                53 F8 FF  FF 7F F8 FF FF 7F 77 61       S........wa
00C0: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x00B5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wai0" with entities [EventEntity, EventEntity]
  1: 0x00C2 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C3   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68     f..........th
00D0: 6B 31 00                                          k1.             
```

#### Opcodes

```
  0: 0x00C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31     S........thk1
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   f..........thk2
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    53 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 00      S........thk2. 
```

#### Opcodes

```
  0: 0x00F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               66                 f
0100: 00 80 F8 FF FF 7F F8 FF  FF 7F 6F 62 69 30 00     ..........obi0. 
```

#### Opcodes

```
  0: 0x00FF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "obi0" with entities [EventEntity, EventEntity], work=40*
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               53                 S
0110: F8 FF FF 7F F8 FF FF 7F  6F 62 69 30 00           ........obi0.   
```

#### Opcodes

```
  0: 0x010F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "obi0" with entities [EventEntity, EventEntity]
  1: 0x011C [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         66 00 80               f..
0120: F8 FF FF 7F F8 FF FF 7F  6F 62 69 31 00           ........obi1.   
```

#### Opcodes

```
  0: 0x011D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "obi1" with entities [EventEntity, EventEntity], work=40*
  1: 0x012C [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         53 F8 FF               S..
0130: FF 7F F8 FF FF 7F 6F 62  69 31 00                 ......obi1.     
```

#### Opcodes

```
  0: 0x012D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "obi1" with entities [EventEntity, EventEntity]
  1: 0x013A [0x00] END_REQSTACK()
```

### Event 502

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013B   |
| Data Size    | 55 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   1E F0 FF FF 7F             .....
0140: 6F 70 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  opf..........tlk
0150: 30 1D 03 80 23 02 03 10  04 80 00 61 01 1D 05 80  0...#......a....
0160: 23 66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31  #f..........tlk1
0170: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x013B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0140 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0141 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0142 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0151 [0x1D] PRINT_EVENT_MESSAGE(message_id=8042*)
    → "My heartaru goes out to all you pioneers. As if the dangers of the jungle weren't enough, you've also got to contend with the foul beasts within. It's a position I certainly do not envy-wenvy."
  5: 0x0154 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0155 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0161
  7: 0x015D [0x1D] PRINT_EVENT_MESSAGE(message_id=8043*)
    → "A warm smile and a pataru on the back is all I am able to provide, but Elmric at the south side of tent-went may be able to give you more."
  8: 0x0160 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0161 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 10: 0x0170 [0x21] END_EVENT
 11: 0x0171 [0x00] END_REQSTACK()
```

### Event 20

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0172  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:       00                                            .             
```

#### Opcodes

```
  0: 0x0172 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0173   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:          37 06 80 07 80  08 80 09 80 00              7.........   
```

#### Opcodes

```
  0: 0x0173 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=368.700*, z=179.615*, y=0.361*, direction=292.3°*
  1: 0x017C [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                         37 0A 80               7..
0180: 0B 80 0C 80 0D 80 00                              .......         
```

#### Opcodes

```
  0: 0x017D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=374.908*, z=170.272*, y=0.380*, direction=150.5°*
  1: 0x0186 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0187   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                      32  00 80 1F 00 0E 80 0F 80         2........
0190: 10 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0187 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x018A [0x1F] MOVE_ENTITY: EventEntity moves to X=373.349*, Z=174.079*, Y=0.509*
  2: 0x0192 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0194 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0195   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                32 11 80  1F 00 12 80 13 80 14 80       2..........
01A0: 1F 01 1E 1C 52 10 01 6F  70 00                    ....R..op.      
```

#### Opcodes

```
  0: 0x0195 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0198 [0x1F] MOVE_ENTITY: EventEntity moves to X=375.536*, Z=168.468*, Y=0.333*
  2: 0x01A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01A2 [0x1E] EventEntity looks at Elmric (ID: 17846812/0x0110521C) and starts talking
  4: 0x01A7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x01A8 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x01A9 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01AA   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:                                32 11 80 1F 00 15            2.....
01B0: 80 16 80 17 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x01AA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01AD [0x1F] MOVE_ENTITY: EventEntity moves to X=377.784*, Z=167.934*, Y=0.434*
  2: 0x01B5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01B7 [0x00] END_REQSTACK()
```
