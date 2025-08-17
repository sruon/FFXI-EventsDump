# 17776668 - Kurou-Morou

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 548 bytes             |
| Total Events     | 20                    |
| References Count | 36                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      4 |              2 |
| [197](#event-197)          | 0x0004       |     10 |              2 |
| [198](#event-198)          | 0x000E       |      1 |              1 |
| [65535.1](#event-655351)   | 0x000F       |     12 |              3 |
| [65535.2](#event-655352)   | 0x001B       |     12 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     12 |              4 |
| [65535.4](#event-655354)   | 0x0033       |     12 |              3 |
| [65535.5](#event-655355)   | 0x003F       |     24 |              6 |
| [65535.6](#event-655356)   | 0x0057       |     28 |              8 |
| [65535.7](#event-655357)   | 0x0073       |     10 |              2 |
| [65535.8](#event-655358)   | 0x007D       |      3 |              2 |
| [65535.9](#event-655359)   | 0x0080       |     12 |              3 |
| [65535.10](#event-6553510) | 0x008C       |     11 |              3 |
| [65535.11](#event-6553511) | 0x0097       |     32 |              7 |
| [65535.12](#event-6553512) | 0x00B7       |     19 |              3 |
| [65535.13](#event-6553513) | 0x00CA       |     29 |              3 |
| [65535.14](#event-6553514) | 0x00E7       |      9 |              3 |
| [65535.15](#event-6553515) | 0x00F0       |     29 |              3 |
| [65535.16](#event-6553516) | 0x010D       |     29 |              3 |
| [65535.17](#event-6553517) | 0x012A       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFEF76A  |  4294899562 |
|       2 | 0xE9A6      |       59814 |
|       3 | 0xFFFFFB46  |  4294966086 |
|       4 | 0x0701      |        1793 |
|       5 | 0xFFFEF4FE  |  4294898942 |
|       6 | 0xEAD2      |       60114 |
|       7 | 0x0987      |        2439 |
|       8 | 0xFFFEEF74  |  4294897524 |
|       9 | 0xEF71      |       61297 |
|      10 | 0xFFFEEB38  |  4294896440 |
|      11 | 0xF464      |       62564 |
|      12 | 0xFFFFFB50  |  4294966096 |
|      13 | 0xFFFEFE3C  |  4294901308 |
|      14 | 0xED3E      |       60734 |
|      15 | 0xFFFFFB51  |  4294966097 |
|      16 | 0x0689      |        1673 |
|      17 | 0x0028      |          40 |
|      18 | 0xFFFEF759  |  4294899545 |
|      19 | 0xE941      |       59713 |
|      20 | 0xFFFEEA77  |  4294896247 |
|      21 | 0xF075      |       61557 |
|      22 | 0xFFFEEAFB  |  4294896379 |
|      23 | 0xF0F9      |       61689 |
|      24 | 0x0A4D      |        2637 |
|      25 | 0xFFFEE5DD  |  4294895069 |
|      26 | 0xF818      |       63512 |
|      27 | 0x0DBD      |        3517 |
|      28 | 0xFFFEEBD3  |  4294896595 |
|      29 | 0xEE56      |       61014 |
|      30 | 0x0986      |        2438 |
|      31 | 0xFFFF1225  |  4294906405 |
|      32 | 0xF989      |       63881 |
|      33 | 0x0000      |           0 |
|      34 | 0x001E      |          30 |
|      35 | 0x003C      |          60 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 32 00 80 00                                       2...            
```

#### Opcodes

```
  0: 0x0000 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 197

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             37 01 80 02  80 03 80 04 80 00            7.........  
```

#### Opcodes

```
  0: 0x0004 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-67.734*, z=59.814*, y=-1.210*, direction=157.6°*
  1: 0x000D [0x00] END_REQSTACK()
```

### Event 198

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            00                   . 
```

#### Opcodes

```
  0: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               22                 "
0010: 00 37 05 80 06 80 03 80  07 80 00                 .7.........     
```

#### Opcodes

```
  0: 0x000F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0011 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-68.354*, z=60.114*, y=-1.210*, direction=214.4°*
  2: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1F 00 08 80 09             .....
0020: 80 03 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=-69.772*, Z=61.297*, Y=-1.210*
  1: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      1F  00 0A 80 0B 80 0C 80 1F         .........
0030: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-70.856*, Z=62.564*, Y=-1.200*
  1: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0031 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          22 00 37 0D 80  0E 80 0F 80 10 80 00        ".7......... 
```

#### Opcodes

```
  0: 0x0033 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-65.988*, z=60.734*, y=-1.199*, direction=147.0°*
  2: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               32                 2
0040: 11 80 1F 00 12 80 13 80  03 80 1F 01 1F 00 14 80  ................
0050: 15 80 03 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x003F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=-67.751*, Z=59.713*, Y=-1.210*
  2: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004C [0x1F] MOVE_ENTITY: EventEntity moves to X=-71.049*, Z=61.557*, Y=-1.210*
  4: 0x0054 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      37  16 80 17 80 03 80 18 80         7........
0060: 1F 00 19 80 1A 80 0C 80  1F 01 6F 1E 1B 40 0F 01  ..........o..@..
0070: 6F 70 00                                          op.             
```

#### Opcodes

```
  0: 0x0057 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-70.917*, z=61.689*, y=-1.210*, direction=231.8°*
  1: 0x0060 [0x1F] MOVE_ENTITY: EventEntity moves to X=-72.227*, Z=63.512*, Y=-1.200*
  2: 0x0068 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006B [0x1E] EventEntity looks at Ilumida (ID: 17776667/0x010F401B) and starts talking
  5: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0071 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          37 19 80 1A 80  0C 80 1B 80 00              7.........   
```

#### Opcodes

```
  0: 0x0073 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-72.227*, z=63.512*, y=-1.200*, direction=309.1°*
  1: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007D  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         22 01 00               "..
```

#### Opcodes

```
  0: 0x007D [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0080   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: 22 00 37 19 80 1A 80 0C  80 1B 80 00              ".7.........    
```

#### Opcodes

```
  0: 0x0080 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0082 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-72.227*, z=63.512*, y=-1.200*, direction=309.1°*
  2: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      1F 00 1C 80              ....
0090: 1D 80 03 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x008C [0x1F] MOVE_ENTITY: EventEntity moves to X=-70.701*, Z=61.014*, Y=-1.210*
  1: 0x0094 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0096 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0097   |
| Data Size    | 32 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      37  14 80 15 80 03 80 1E 80         7........
00A0: 1F 00 12 80 13 80 03 80  1F 01 1F 00 1F 80 20 80  .............. .
00B0: 21 80 1F 01 22 01 00                              !..."..         
```

#### Opcodes

```
  0: 0x0097 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-71.049*, z=61.557*, y=-1.210*, direction=214.3°*
  1: 0x00A0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-67.751*, Z=59.713*, Y=-1.210*
  2: 0x00A8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AA [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.891*, Z=63.881*, Y=0.000*
  4: 0x00B2 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00B4 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      66  11 80 F8 FF FF 7F F8 FF         f........
00C0: FF 7F 74 6C 6B 30 1C 22  80 00                    ..tlk0."..      
```

#### Opcodes

```
  0: 0x00B7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00C6 [0x1C] WAIT(30* ticks)
  2: 0x00C9 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CA   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                66 11 80 F8 FF FF            f.....
00D0: 7F F8 FF FF 7F 74 68 6B  31 53 F8 FF FF 7F F8 FF  .....thk1S......
00E0: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x00CA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x00D9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x00E6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E7  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      5E  69 64 6C 30 1C 23 80 00         ^idl0.#..
```

#### Opcodes

```
  0: 0x00E7 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00EC [0x1C] WAIT(60* ticks)
  2: 0x00EF [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F0   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0: 66 11 80 F8 FF FF 7F F8  FF FF 7F 69 72 6F 30 53  f..........iro0S
0100: F8 FF FF 7F F8 FF FF 7F  69 72 6F 30 00           ........iro0.   
```

#### Opcodes

```
  0: 0x00F0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "iro0" with entities [EventEntity, EventEntity], work=40*
  1: 0x00FF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "iro0" with entities [EventEntity, EventEntity]
  2: 0x010C [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         66 11 80               f..
0110: F8 FF FF 7F F8 FF FF 7F  64 69 73 30 53 F8 FF FF  ........dis0S...
0120: 7F F8 FF FF 7F 64 69 73  30 00                    .....dis0.      
```

#### Opcodes

```
  0: 0x010D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=40*
  1: 0x011C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  2: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x012A  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                5E 69 64 6C 30 1C            ^idl0.
0130: 23 80 00                                          #..             
```

#### Opcodes

```
  0: 0x012A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x012F [0x1C] WAIT(60* ticks)
  2: 0x0132 [0x00] END_REQSTACK()
```
