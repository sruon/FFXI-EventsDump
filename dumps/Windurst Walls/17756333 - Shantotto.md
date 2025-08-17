# 17756333 - Shantotto

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 596 bytes                |
| Total Events     | 21                       |
| References Count | 15                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [514](#event-514)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     69 |             19 |
| [65535.2](#event-655352)   | 0x0047       |     25 |              3 |
| [65535.3](#event-655353)   | 0x0060       |     37 |              5 |
| [65535.4](#event-655354)   | 0x0085       |     19 |              3 |
| [65535.5](#event-655355)   | 0x0098       |     19 |              3 |
| [65535.6](#event-655356)   | 0x00AB       |     43 |              7 |
| [65535.7](#event-655357)   | 0x00D6       |     19 |              3 |
| [65535.8](#event-655358)   | 0x00E9       |     19 |              3 |
| [65535.9](#event-655359)   | 0x00FC       |     16 |              2 |
| [65535.10](#event-6553510) | 0x010C       |     16 |              2 |
| [65535.11](#event-6553511) | 0x011C       |     16 |              2 |
| [65535.12](#event-6553512) | 0x012C       |     19 |              3 |
| [65535.13](#event-6553513) | 0x013F       |     16 |              2 |
| [65535.14](#event-6553514) | 0x014F       |     16 |              2 |
| [65535.15](#event-6553515) | 0x015F       |     16 |              2 |
| [65535.16](#event-6553516) | 0x016F       |     16 |              2 |
| [65535.17](#event-6553517) | 0x017F       |     16 |              2 |
| [65535.18](#event-6553518) | 0x018F       |     16 |              2 |
| [65535.19](#event-6553519) | 0x019F       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0006      |           6 |
|       1 | 0x0000      |           0 |
|       2 | 0x00C9      |         201 |
|       3 | 0x055D      |        1373 |
|       4 | 0x00F2      |         242 |
|       5 | 0x0AC8      |        2760 |
|       6 | 0x0019      |          25 |
|       7 | 0x003C      |          60 |
|       8 | 0x0801      |        2049 |
|       9 | 0x00B0      |         176 |
|      10 | 0x0ACE      |        2766 |
|      11 | 0x007C      |         124 |
|      12 | 0x006C      |         108 |
|      13 | 0x001E      |          30 |
|      14 | 0x0044      |          68 |

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

### Event 514

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
| Data Size    | 69 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B7 01 01 00 F8 FF  FF 7F B4 13 00 00 44 2E    ............D.
0010: 40 53 68 61 6E 74 6F 74  74 6F 00 00 00 00 B5 00  @Shantotto......
0020: 00 00 B6 0B 00 80 00 80  01 80 02 80 02 80 02 80  ................
0030: 02 80 01 80 01 80 22 00  92 01 F8 FF FF 7F 94 01  ......".........
0040: F8 FF FF 7F A4 01 00                              .......         
```

#### Opcodes

```
  0: 0x0002 [0xB7] ENTITY_DATA_HANDLER: Set Unknown NPC (ID: 4294443009/0xFFF80001) name from 0x7FFF (monstrosity: 0x13B4)
  1: 0x000C [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x000D [0x00] END_REQSTACK()
     0x000E [0x44] IF_ENTITY_VALID(Unknown NPC (ID: 16430/0x0000402E) valid ? continue : jump_to=0x6853)
     0x0013 [0x61] EventEntity->Render.Flags2 &= ~0x00000001
     0x0015 [0x74] EventEntity->Render.Flags1 |= 0x6F
     0x0017 [0x74] EventEntity->Render.Flags1 |= 0x74
     0x0019 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x001A [0x00] END_REQSTACK()
     0x001B [0x00] END_REQSTACK()
     0x001C [0x00] END_REQSTACK()
     0x001D [0x00] END_REQSTACK()
     0x001E [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
     0x0022 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=6*, hair=6*, head=0*, body=201*, hands=201*, legs=201*, feet=201*, main=0*, sub=0*)
     0x0036 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
     0x0038 [0x92] EventEntity->Render.Flags3 ^= 0x01
     0x003E [0x94] EventEntity->Render.Flags3 ^= 0x01
     0x0044 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
     0x0046 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      B4  13 00 00 6E 61 6D 65 32         ....name2
0050: 00 00 00 00 00 00 00 00  00 00 00 B5 00 00 00 00  ................
```

#### Opcodes

```
  0: 0x0047 [0xB4] UI_WINDOW_STRING_HANDLER(case=0x13 - Copy string and replace @ with space, work_offset=ExtData[1]->WorkLocal[0], string="name2")
  1: 0x005B [0xB5] SET_EVENT_ENTITY_NAME: Change EventEntity name to ExtData[1]->WorkLocal[0]
  2: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 37 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 5B 03 80 F8 FF FF 7F F8  FF FF 7F 67 61 68 32 1C  [..........gah2.
0070: 04 80 5B 05 80 F8 FF FF  7F F8 FF FF 7F 64 6F 6C  ..[..........dol
0080: 30 1C 06 80 00                                    0....           
```

#### Opcodes

```
  0: 0x0060 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gah2" with entities [EventEntity, EventEntity], work=1373*
  1: 0x006F [0x1C] WAIT(242* ticks)
  2: 0x0072 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dol0" with entities [EventEntity, EventEntity], work=2760*
  3: 0x0081 [0x1C] WAIT(25* ticks)
  4: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                5B 03 80  F8 FF FF 7F F8 FF FF 7F       [..........
0090: 67 75 64 30 1C 07 80 00                           gud0....        
```

#### Opcodes

```
  0: 0x0085 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gud0" with entities [EventEntity, EventEntity], work=1373*
  1: 0x0094 [0x1C] WAIT(60* ticks)
  2: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          5B 03 80 F8 FF FF 7F F8          [.......
00A0: FF FF 7F 67 75 64 31 1C  07 80 00                 ...gud1....     
```

#### Opcodes

```
  0: 0x0098 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gud1" with entities [EventEntity, EventEntity], work=1373*
  1: 0x00A7 [0x1C] WAIT(60* ticks)
  2: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 43 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   81 00 F8 FF FF             .....
00B0: 7F 7C 00 F8 FF FF 7F 5B  08 80 F8 FF FF 7F F8 FF  .|.....[........
00C0: FF 7F 79 67 6F 30 1C 09  80 81 01 F8 FF FF 7F 7C  ..ygo0.........|
00D0: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x00AB [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x00B1 [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x00B7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ygo0" with entities [EventEntity, EventEntity], work=2049*
  3: 0x00C6 [0x1C] WAIT(176* ticks)
  4: 0x00C9 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  5: 0x00CF [0x7C] EventEntity->Render.Flags2 |= 0x01
  6: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   5B 0A  80 F8 FF FF 7F F8 FF FF        [.........
00E0: 7F 6B 6B 61 30 1C 0B 80  00                       .kka0....       
```

#### Opcodes

```
  0: 0x00D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kka0" with entities [EventEntity, EventEntity], work=2766*
  1: 0x00E5 [0x1C] WAIT(124* ticks)
  2: 0x00E8 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E9   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                             5B 0A 80 F8 FF FF 7F           [......
00F0: F8 FF FF 7F 6B 6B 61 31  1C 0C 80 00              ....kka1....    
```

#### Opcodes

```
  0: 0x00E9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kka1" with entities [EventEntity, EventEntity], work=2766*
  1: 0x00F8 [0x1C] WAIT(108* ticks)
  2: 0x00FB [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FC   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                      5B 05 80 F8              [...
0100: FF FF 7F F8 FF FF 7F 64  6F 6C 30 00              .......dol0.    
```

#### Opcodes

```
  0: 0x00FC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dol0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x010B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      5B 05 80 F8              [...
0110: FF FF 7F F8 FF FF 7F 64  6F 6C 6C 00              .......doll.    
```

#### Opcodes

```
  0: 0x010C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "doll" with entities [EventEntity, EventEntity], work=2760*
  1: 0x011B [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      5B 05 80 F8              [...
0120: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x011C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x012B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012C   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      5B 05 80 F8              [...
0130: FF FF 7F F8 FF FF 7F 74  6C 6B 31 1C 0D 80 00     .......tlk1.... 
```

#### Opcodes

```
  0: 0x012C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=2760*
  1: 0x013B [0x1C] WAIT(30* ticks)
  2: 0x013E [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               5B                 [
0140: 05 80 F8 FF FF 7F F8 FF  FF 7F 73 6A 69 30 00     ..........sji0. 
```

#### Opcodes

```
  0: 0x013F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sji0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x014E [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                               5B                 [
0150: 05 80 F8 FF FF 7F F8 FF  FF 7F 73 6A 69 31 00     ..........sji1. 
```

#### Opcodes

```
  0: 0x014F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sji1" with entities [EventEntity, EventEntity], work=2760*
  1: 0x015E [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                               5B                 [
0160: 05 80 F8 FF FF 7F F8 FF  FF 7F 73 6A 69 6C 00     ..........sjil. 
```

#### Opcodes

```
  0: 0x015F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sjil" with entities [EventEntity, EventEntity], work=2760*
  1: 0x016E [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                               5B                 [
0170: 05 80 F8 FF FF 7F F8 FF  FF 7F 6F 68 68 30 00     ..........ohh0. 
```

#### Opcodes

```
  0: 0x016F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohh0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x017E [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                               5B                 [
0180: 05 80 F8 FF FF 7F F8 FF  FF 7F 6F 68 68 31 00     ..........ohh1. 
```

#### Opcodes

```
  0: 0x017F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohh1" with entities [EventEntity, EventEntity], work=2760*
  1: 0x018E [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                               5B                 [
0190: 05 80 F8 FF FF 7F F8 FF  FF 7F 6F 68 68 6C 00     ..........ohhl. 
```

#### Opcodes

```
  0: 0x018F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ohhl" with entities [EventEntity, EventEntity], work=2760*
  1: 0x019E [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019F   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               5B                 [
01A0: 05 80 F8 FF FF 7F F8 FF  FF 7F 73 6F 68 30 1C 0E  ..........soh0..
01B0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x019F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "soh0" with entities [EventEntity, EventEntity], work=2760*
  1: 0x01AE [0x1C] WAIT(68* ticks)
  2: 0x01B1 [0x00] END_REQSTACK()
```
