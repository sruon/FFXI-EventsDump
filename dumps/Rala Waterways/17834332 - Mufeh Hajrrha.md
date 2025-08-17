# 17834332 - Mufeh Hajrrha

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 588 bytes                |
| Total Events     | 19                       |
| References Count | 22                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [376](#event-376)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     16 |              5 |
| [65535.3](#event-655353)   | 0x0020       |     25 |              3 |
| [65535.4](#event-655354)   | 0x0039       |     25 |              3 |
| [65535.5](#event-655355)   | 0x0052       |     33 |              3 |
| [65535.6](#event-655356)   | 0x0073       |     33 |              3 |
| [65535.7](#event-655357)   | 0x0094       |     33 |              3 |
| [65535.8](#event-655358)   | 0x00B5       |     33 |              3 |
| [65535.9](#event-655359)   | 0x00D6       |     33 |              3 |
| [65535.10](#event-6553510) | 0x00F7       |     33 |              3 |
| [65535.11](#event-6553511) | 0x0118       |     16 |              4 |
| [65535.12](#event-6553512) | 0x0128       |     16 |              4 |
| [65535.13](#event-6553513) | 0x0138       |     16 |              4 |
| [65535.14](#event-6553514) | 0x0148       |     16 |              4 |
| [65535.15](#event-6553515) | 0x0158       |     16 |              4 |
| [65535.16](#event-6553516) | 0x0168       |     33 |              3 |
| [65535.17](#event-6553517) | 0x0189       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFDB27E  |  4294816382 |
|       2 | 0x5B09      |       23305 |
|       3 | 0xFFFFE97B  |  4294961531 |
|       4 | 0xFFFD8CE5  |  4294806757 |
|       5 | 0x514D      |       20813 |
|       6 | 0x003B      |          59 |
|       7 | 0x0064      |         100 |
|       8 | 0x00C7      |         199 |
|       9 | 0x005C      |          92 |
|      10 | 0x0068      |         104 |
|      11 | 0x0001      |           1 |
|      12 | 0x0078      |         120 |
|      13 | 0x0007      |           7 |
|      14 | 0x003C      |          60 |
|      15 | 0x0025      |          37 |
|      16 | 0x0082      |         130 |
|      17 | 0x0015      |          21 |
|      18 | 0x0023      |          35 |
|      19 | 0x007C      |         124 |
|      20 | 0x0038      |          56 |
|      21 | 0x001E      |          30 |

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

### Event 376

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-150.914*, Z=23.305*, Y=-5.765*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 00 80 1F 00 04 80 05  80 03 80 1F 01 22 01 00  2............"..
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=-160.539*, Z=20.813*, Y=-5.765*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: B4 00 00 00 3F 3F 3F 00  00 00 00 00 00 00 00 00  ....???.........
0030: 00 00 00 00 B5 00 00 00  00                       .........       
```

#### Opcodes

```
  0: 0x0020 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x00 - Copy string from opcode, work_offset=ExtData[1]->WorkLocal[0], string="???")
  1: 0x0034 [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             B4 13 00 00 4D 75 66           ....Muf
0040: 65 68 40 48 61 6A 72 72  68 61 00 00 00 B5 00 00  eh@Hajrrha......
0050: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x0039 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="Mufeh@Hajrrha")
  1: 0x004D [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       5F 06 06 80 F8 FF  FF 7F F8 FF FF 7F 74 6C    _...........tl
0060: 6B 30 07 80 5F 07 F8 FF  FF 7F F8 FF FF 7F 74 6C  k0.._.........tl
0070: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x0052 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=59*, entity1=EventEntity, entity2=EventEntity, string="tlk0", extra=100*)
  1: 0x0064 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          5F 06 06 80 F8  FF FF 7F F8 FF FF 7F 74     _...........t
0080: 6C 6B 31 07 80 5F 07 F8  FF FF 7F F8 FF FF 7F 74  lk1.._.........t
0090: 6C 6B 31 00                                       lk1.            
```

#### Opcodes

```
  0: 0x0073 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=59*, entity1=EventEntity, entity2=EventEntity, string="tlk1", extra=100*)
  1: 0x0085 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             5F 06 06 80  F8 FF FF 7F F8 FF FF 7F      _...........
00A0: 74 68 6B 31 07 80 5F 07  F8 FF FF 7F F8 FF FF 7F  thk1.._.........
00B0: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0094 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=59*, entity1=EventEntity, entity2=EventEntity, string="thk1", extra=100*)
  1: 0x00A6 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                5F 06 06  80 F8 FF FF 7F F8 FF FF       _..........
00C0: 7F 74 68 6B 32 07 80 5F  07 F8 FF FF 7F F8 FF FF  .thk2.._........
00D0: 7F 74 68 6B 32 00                                 .thk2.          
```

#### Opcodes

```
  0: 0x00B5 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=59*, entity1=EventEntity, entity2=EventEntity, string="thk2", extra=100*)
  1: 0x00C7 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   5F 06  08 80 F8 FF FF 7F F8 FF        _.........
00E0: FF 7F 74 6C 6B 30 09 80  5F 07 F8 FF FF 7F F8 FF  ..tlk0.._.......
00F0: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x00D6 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=199*, entity1=EventEntity, entity2=EventEntity, string="tlk0", extra=92*)
  1: 0x00E8 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F7   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      5F  06 08 80 F8 FF FF 7F F8         _........
0100: FF FF 7F 74 6C 6B 31 0A  80 5F 07 F8 FF FF 7F F8  ...tlk1.._......
0110: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x00F7 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=199*, entity1=EventEntity, entity2=EventEntity, string="tlk1", extra=104*)
  1: 0x0109 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0117 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0118   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                          6E F8 FF FF 7F 0B 80 99          n.......
0120: F8 FF FF 7F 1C 0C 80 00                           ........        
```

#### Opcodes

```
  0: 0x0118 [0x6E] EventEntity uses emote 1*
  1: 0x011F [0x99] Wait for EventEntity animation to complete
  2: 0x0124 [0x1C] WAIT(120* ticks)
  3: 0x0127 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0128   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                          6E F8 FF FF 7F 0D 80 99          n.......
0130: F8 FF FF 7F 1C 0E 80 00                           ........        
```

#### Opcodes

```
  0: 0x0128 [0x6E] EventEntity uses emote 7*
  1: 0x012F [0x99] Wait for EventEntity animation to complete
  2: 0x0134 [0x1C] WAIT(60* ticks)
  3: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          6E F8 FF FF 7F 0F 80 99          n.......
0140: F8 FF FF 7F 1C 10 80 00                           ........        
```

#### Opcodes

```
  0: 0x0138 [0x6E] EventEntity uses emote 37*
  1: 0x013F [0x99] Wait for EventEntity animation to complete
  2: 0x0144 [0x1C] WAIT(130* ticks)
  3: 0x0147 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0148   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          6E F8 FF FF 7F 11 80 99          n.......
0150: F8 FF FF 7F 1C 10 80 00                           ........        
```

#### Opcodes

```
  0: 0x0148 [0x6E] EventEntity uses emote 21*
  1: 0x014F [0x99] Wait for EventEntity animation to complete
  2: 0x0154 [0x1C] WAIT(130* ticks)
  3: 0x0157 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0158   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          6E F8 FF FF 7F 12 80 99          n.......
0160: F8 FF FF 7F 1C 10 80 00                           ........        
```

#### Opcodes

```
  0: 0x0158 [0x6E] EventEntity uses emote 35*
  1: 0x015F [0x99] Wait for EventEntity animation to complete
  2: 0x0164 [0x1C] WAIT(130* ticks)
  3: 0x0167 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0168   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                          5F 06 13 80 F8 FF FF 7F          _.......
0170: F8 FF FF 7F 70 6F 73 30  14 80 5F 07 F8 FF FF 7F  ....pos0.._.....
0180: F8 FF FF 7F 70 6F 73 30  00                       ....pos0.       
```

#### Opcodes

```
  0: 0x0168 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=124*, entity1=EventEntity, entity2=EventEntity, string="pos0", extra=56*)
  1: 0x017A [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0188 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0189   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                             6B 69 64 6C 30 F8 FF           kidl0..
0190: FF 7F 1C 15 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0189 [0x6B] STOP_AND_IDLE: EventEntity stops current action and resets to idle (animation="idl0")
  1: 0x0192 [0x1C] WAIT(30* ticks)
  2: 0x0195 [0x00] END_REQSTACK()
```
