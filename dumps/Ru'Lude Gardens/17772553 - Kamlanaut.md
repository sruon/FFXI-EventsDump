# 17772553 - Kamlanaut

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 500 bytes                 |
| Total Events     | 26                        |
| References Count | 13                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     12 |              3 |
| [65](#event-65)            | 0x000C       |     31 |              5 |
| [128](#event-128)          | 0x002B       |      3 |              2 |
| [60](#event-60)            | 0x002E       |      3 |              2 |
| [65535.1](#event-655351)   | 0x0031       |     29 |              3 |
| [65535.2](#event-655352)   | 0x004E       |     19 |              3 |
| [65535.3](#event-655353)   | 0x0061       |     29 |              3 |
| [65535.4](#event-655354)   | 0x007E       |     19 |              3 |
| [65535.5](#event-655355)   | 0x0091       |     29 |              3 |
| [65535.6](#event-655356)   | 0x00AE       |     24 |              4 |
| [65535.7](#event-655357)   | 0x00C6       |     34 |              4 |
| [65535.8](#event-655358)   | 0x00E8       |      9 |              3 |
| [65535.9](#event-655359)   | 0x00F1       |      1 |              1 |
| [65535.10](#event-6553510) | 0x00F2       |      1 |              1 |
| [65535.11](#event-6553511) | 0x00F3       |     18 |              4 |
| [65535.12](#event-6553512) | 0x0105       |     10 |              2 |
| [65535.13](#event-6553513) | 0x010F       |      9 |              3 |
| [65535.14](#event-6553514) | 0x0118       |      9 |              3 |
| [65535.15](#event-6553515) | 0x0121       |     10 |              2 |
| [65535.16](#event-6553516) | 0x012B       |     10 |              2 |
| [10188](#event-10188)      | 0x0135       |      4 |              2 |
| [10189](#event-10189)      | 0x0139       |      4 |              2 |
| [10190](#event-10190)      | 0x013D       |      4 |              2 |
| [65535.17](#event-6553517) | 0x0141       |      2 |              2 |
| [10199](#event-10199)      | 0x0143       |      1 |              1 |
| [10200](#event-10200)      | 0x0144       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x1737C     |       95100 |
|       2 | 0xFFFFE230  |  4294959664 |
|       3 | 0x0400      |        1024 |
|       4 | 0x0000      |           0 |
|       5 | 0x006A      |         106 |
|       6 | 0x0069      |         105 |
|       7 | 0x001E      |          30 |
|       8 | 0x0078      |         120 |
|       9 | 0x003C      |          60 |
|      10 | 0x0001      |           1 |
|      11 | 0x0080      |         128 |
|      12 | 0x0002      |           2 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 33 01 37 00 80 01 80 02  80 03 80 00              3.7.........    
```

#### Opcodes

```
  0: 0x0000 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.050*, z=95.100*, y=-7.632*, direction=90.0°*
  2: 0x000B [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 31 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      6C F8 FF FF              l...
0010: 7F 04 80 04 80 92 01 F8  FF FF 7F 4E 00 F8 FF FF  ...........N....
0020: 7F 37 00 80 01 80 02 80  03 80 00                 .7.........     
```

#### Opcodes

```
  0: 0x000C [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0015 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x001B [0x4E] SET_ENTITY_HIDE_FLAG: Show EventEntity
  3: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.050*, z=95.100*, y=-7.632*, direction=90.0°*
  4: 0x002A [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   22 00 00                   "..  
```

#### Opcodes

```
  0: 0x002B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            22 00                ".
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x002E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    5B 05 80 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30   [..........pas0
0040: 53 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 00        S........pas0.  
```

#### Opcodes

```
  0: 0x0031 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=106*
  1: 0x0040 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            5B 06                [.
0050: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1C 07 80  .........tlk0...
0060: 00                                                .               
```

#### Opcodes

```
  0: 0x004E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=105*
  1: 0x005D [0x1C] WAIT(30* ticks)
  2: 0x0060 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0061   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:    5B 06 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 31   [..........tlk1
0070: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 00        S........tlk1.  
```

#### Opcodes

```
  0: 0x0061 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=105*
  1: 0x0070 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            5B 06                [.
0080: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 1C 07 80  .........thk1...
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x007E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=105*
  1: 0x008D [0x1C] WAIT(30* ticks)
  2: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    5B 06 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   [..........thk2
00A0: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        S........thk2.  
```

#### Opcodes

```
  0: 0x0091 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=105*
  1: 0x00A0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 24 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            5B 06                [.
00B0: 80 F8 FF FF 7F F8 FF FF  7F 73 69 74 31 1C 08 80  .........sit1...
00C0: 5E 69 64 6C 30 00                                 ^idl0.          
```

#### Opcodes

```
  0: 0x00AE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sit1" with entities [EventEntity, EventEntity], work=105*
  1: 0x00BD [0x1C] WAIT(120* ticks)
  2: 0x00C0 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  3: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 34 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   5B 06  80 F8 FF FF 7F F8 FF FF        [.........
00D0: 7F 73 69 74 30 53 F8 FF  FF 7F F8 FF FF 7F 73 69  .sit0S........si
00E0: 74 30 5E 64 66 74 30 00                           t0^dft0.        
```

#### Opcodes

```
  0: 0x00C6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sit0" with entities [EventEntity, EventEntity], work=105*
  1: 0x00D5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sit0" with entities [EventEntity, EventEntity]
  2: 0x00E2 [0x5E] EventEntity goes idle (kills current action) (animation: "dft0")
  3: 0x00E7 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E8  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                          5E 64 66 74 30 1C 09 80          ^dft0...
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E8 [0x5E] EventEntity goes idle (kills current action) (animation: "dft0")
  1: 0x00ED [0x1C] WAIT(60* ticks)
  2: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    00                                              .              
```

#### Opcodes

```
  0: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00F2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       00                                            .             
```

#### Opcodes

```
  0: 0x00F2 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F3   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:          22 00 2F 00 F8  FF FF 7F 6C F8 FF FF 7F     "./.....l....
0100: 04 80 0A 80 00                                    .....           
```

#### Opcodes

```
  0: 0x00F3 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00F5 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x00FB [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0104 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0105   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                6C F8 FF  FF 7F 0B 80 0A 80 00          l......... 
```

#### Opcodes

```
  0: 0x0105 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010F  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               22                 "
0110: 00 2F 00 F8 FF FF 7F 00                           ./......        
```

#### Opcodes

```
  0: 0x010F [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0111 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0117 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0118  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          22 01 2F 01 F8 FF FF 7F          "./.....
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0118 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x011A [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x0120 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    6C F8 FF FF 7F 04 80  0A 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0121 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x012A [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                   6C F8 FF FF 7F             l....
0130: 0B 80 0A 80 00                                    .....           
```

#### Opcodes

```
  0: 0x012B [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0134 [0x00] END_REQSTACK()
```

### Event 10188

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0135  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                95 0C 80  00                            ....       
```

#### Opcodes

```
  0: 0x0135 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  1: 0x0138 [0x00] END_REQSTACK()
```

### Event 10189

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0139  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                             95 0C 80 00                    ....   
```

#### Opcodes

```
  0: 0x0139 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  1: 0x013C [0x00] END_REQSTACK()
```

### Event 10190

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013D  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         95 0C 80               ...
0140: 00                                                .               
```

#### Opcodes

```
  0: 0x013D [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  1: 0x0140 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0141  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:    96 00                                           ..             
```

#### Opcodes

```
  0: 0x0141 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x0142 [0x00] END_REQSTACK()
```

### Event 10199

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0143  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:          00                                          .            
```

#### Opcodes

```
  0: 0x0143 [0x00] END_REQSTACK()
```

### Event 10200

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0144  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:             00                                        .           
```

#### Opcodes

```
  0: 0x0144 [0x00] END_REQSTACK()
```
