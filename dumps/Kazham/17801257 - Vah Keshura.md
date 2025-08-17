# 17801257 - Vah Keshura

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 772 bytes        |
| Total Events     | 27               |
| References Count | 17               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     42 |              4 |
| [65535.3](#event-655353)   | 0x003B       |     16 |              2 |
| [65535.4](#event-655354)   | 0x004B       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0059       |     22 |              3 |
| [65535.6](#event-655356)   | 0x006F       |     14 |              2 |
| [65535.7](#event-655357)   | 0x007D       |     16 |              2 |
| [65535.8](#event-655358)   | 0x008D       |     20 |              3 |
| [65535.9](#event-655359)   | 0x00A1       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00B1       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00BF       |     16 |              2 |
| [65535.12](#event-6553512) | 0x00CF       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00DD       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00ED       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00FB       |     16 |              2 |
| [65535.16](#event-6553516) | 0x010B       |     14 |              2 |
| [65535.17](#event-6553517) | 0x0119       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0129       |     14 |              2 |
| [65535.19](#event-6553519) | 0x0137       |      9 |              3 |
| [124](#event-124)          | 0x0140       |     33 |             12 |
| [187](#event-187)          | 0x0161       |     33 |             12 |
| [130](#event-130)          | 0x0182       |     25 |              8 |
| [65535.20](#event-6553520) | 0x019B       |     37 |              9 |
| [65535.21](#event-6553521) | 0x01C0       |     37 |              9 |
| [131](#event-131)          | 0x01E5       |     47 |             14 |
| [132](#event-132)          | 0x0214       |     47 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x0008      |           8 |
|       2 | 0x0034      |          52 |
|       3 | 0x0035      |          53 |
|       4 | 0x001E      |          30 |
|       5 | 0x2758      |       10072 |
|       6 | 0x2759      |       10073 |
|       7 | 0x2886      |       10374 |
|       8 | 0x2887      |       10375 |
|       9 | 0x27DC      |       10204 |
|      10 | 0x27DD      |       10205 |
|      11 | 0x27DE      |       10206 |
|      12 | 0x27DF      |       10207 |
|      13 | 0x27E0      |       10208 |
|      14 | 0x27E1      |       10209 |
|      15 | 0x27E2      |       10210 |
|      16 | 0x27E3      |       10211 |

## String References

- **10072**: Ah, I love how my blades shine when wielded in the moonlight.
- **10073**: And not just shine...my daggerrrs cut so well that even the chieftainness asked me forrr one...no, two!
- **10204**: You say you want a Tonberry knife?
- **10205**: Hah-hah! I get it! You want to be a chef, and hearrrd that Tonberry knives are the best in Vana'diel, rrright?
- **10206**: But there's no way even the finest chef could use one of those. They're way too dangerrrous!
- **10207**: But if you still want one anyway, you're going to have to go to the Temple of Uggalepih. They say that there's a kitchen there where an evil chef spends his days and nights sharrrpening his knives.
- **10208**: If you still want a Tonberry knife, you're going to have to go to the Temple of Uggalepih.
- **10209**: You'll find plenty of knives in the kitchen, but keep a "sharrrp" lookout for the chef! Nya-ha-ha!
- **10210**: Wow, you rrreally got one! You're the only person I know who would want to get within twenty feet of one of those.
- **10211**: Hey, you're not going to trrry using that thing, are you?
- **10374**: Ah, I love how my blades shine when wielded in the moonlight.
- **10375**: But if you do not get your rrreeking tail out of my sight, I won't wait until the moon's out to show you how sharp they are.

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 42 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 66 00   S........tlk0f.
0020: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 32 53 F8 FF  .........tlk2S..
0030: FF 7F F8 FF FF 7F 74 6C  6B 32 00                 ......tlk2.     
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=50*
  2: 0x002D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   66 01 80 F8 FF             f....
0040: FF 7F F8 FF FF 7F 75 72  65 30 00                 ......ure0.     
```

#### Opcodes

```
  0: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ure0" with entities [EventEntity, EventEntity], work=8*
  1: 0x004A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                   53 F8 FF FF 7F             S....
0050: F8 FF FF 7F 75 72 65 30  00                       ....ure0.       
```

#### Opcodes

```
  0: 0x004B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ure0" with entities [EventEntity, EventEntity]
  1: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             81 00 F8 FF FF 7F 66           ......f
0060: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 00     ..........thk1. 
```

#### Opcodes

```
  0: 0x0059 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x005F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
  2: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               53                 S
0070: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 00           ........thk1.   
```

#### Opcodes

```
  0: 0x006F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         66 00 80               f..
0080: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 00           ........thk2.   
```

#### Opcodes

```
  0: 0x007D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
  1: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         53 F8 FF               S..
0090: FF 7F F8 FF FF 7F 74 68  6B 32 81 01 F8 FF FF 7F  ......thk2......
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x008D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x009A [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    66 02 80 F8 FF FF 7F  F8 FF FF 7F 64 69 73 30   f..........dis0
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00A1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
  1: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    53 F8 FF FF 7F F8 FF  FF 7F 64 69 73 30 00      S........dis0. 
```

#### Opcodes

```
  0: 0x00B1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               66                 f
00C0: 02 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 63 30 00     ..........tlc0. 
```

#### Opcodes

```
  0: 0x00BF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=52*
  1: 0x00CE [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                               53                 S
00D0: F8 FF FF 7F F8 FF FF 7F  74 6C 63 30 00           ........tlc0.   
```

#### Opcodes

```
  0: 0x00CF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc0" with entities [EventEntity, EventEntity]
  1: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         66 02 80               f..
00E0: F8 FF FF 7F F8 FF FF 7F  74 6C 63 31 00           ........tlc1.   
```

#### Opcodes

```
  0: 0x00DD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=52*
  1: 0x00EC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00ED   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                         53 F8 FF               S..
00F0: FF 7F F8 FF FF 7F 74 6C  63 31 00                 ......tlc1.     
```

#### Opcodes

```
  0: 0x00ED [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  1: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   66 03 80 F8 FF             f....
0100: FF 7F F8 FF FF 7F 74 6C  62 31 00                 ......tlb1.     
```

#### Opcodes

```
  0: 0x00FB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  1: 0x010A [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   53 F8 FF FF 7F             S....
0110: F8 FF FF 7F 74 6C 62 31  00                       ....tlb1.       
```

#### Opcodes

```
  0: 0x010B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  1: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0119   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             66 03 80 F8 FF FF 7F           f......
0120: F8 FF FF 7F 74 6C 62 32  00                       ....tlb2.       
```

#### Opcodes

```
  0: 0x0119 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
  1: 0x0128 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0129   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                             53 F8 FF FF 7F F8 FF           S......
0130: FF 7F 74 6C 62 32 00                              ..tlb2.         
```

#### Opcodes

```
  0: 0x0129 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb2" with entities [EventEntity, EventEntity]
  1: 0x0136 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0137  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      5E  69 64 6C 30 1C 04 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0137 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x013C [0x1C] WAIT(30* ticks)
  2: 0x013F [0x00] END_REQSTACK()
```

### Event 124

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0140   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140: 1E F0 FF FF 7F 6F 70 29  08 29 A0 0F 01 01 1D 05  .....op).)......
0150: 80 23 1D 06 80 23 29 08  29 A0 0F 01 02 20 00 21  .#...#).).... .!
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x0140 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0145 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0146 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0147 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x01)
  4: 0x014E [0x1D] PRINT_EVENT_MESSAGE(message_id=10072*)
    → "Ah, I love how my blades shine when wielded in the moonlight."
  5: 0x0151 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0152 [0x1D] PRINT_EVENT_MESSAGE(message_id=10073*)
    → "And not just shine...my daggerrrs cut so well that even the chieftainness asked me forrr one...no, two!"
  7: 0x0155 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0156 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x02)
  9: 0x015D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x015F [0x21] END_EVENT
 11: 0x0160 [0x00] END_REQSTACK()
```

### Event 187

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0161   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:    1E F0 FF FF 7F 6F 70  29 08 29 A0 0F 01 01 1D   .....op).).....
0170: 07 80 23 1D 08 80 23 29  08 29 A0 0F 01 02 20 00  ..#...#).).... .
0180: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0161 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0166 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0167 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0168 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x01)
  4: 0x016F [0x1D] PRINT_EVENT_MESSAGE(message_id=10374*)
    → "Ah, I love how my blades shine when wielded in the moonlight."
  5: 0x0172 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0173 [0x1D] PRINT_EVENT_MESSAGE(message_id=10375*)
    → "But if you do not get your rrreeking tail out of my sight, I won't wait until the moon's out to show you how sharp they are."
  7: 0x0176 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0177 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x02)
  9: 0x017E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0180 [0x21] END_EVENT
 11: 0x0181 [0x00] END_REQSTACK()
```

### Event 130

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0182   |
| Data Size    | 25 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:       1E F0 FF FF 7F 6F  70 29 0B 29 A0 0F 01 17    .....op).)....
0190: 29 0B 29 A0 0F 01 18 20  00 21 00                 ).).... .!.     
```

#### Opcodes

```
  0: 0x0182 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0187 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0188 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0189 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x17)
  4: 0x0190 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x18)
  5: 0x0197 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0199 [0x21] END_EVENT
  7: 0x019A [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019B   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                   29 08 29 A0 0F             ).)..
01A0: 01 05 1D 09 80 23 29 08  29 A0 0F 01 06 29 08 29  .....#).)....).)
01B0: A0 0F 01 07 1D 0A 80 23  29 08 29 A0 0F 01 08 00  .......#).).....
```

#### Opcodes

```
  0: 0x019B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x05)
  1: 0x01A2 [0x1D] PRINT_EVENT_MESSAGE(message_id=10204*)
    → "You say you want a Tonberry knife?"
  2: 0x01A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01A6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x06)
  4: 0x01AD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x07)
  5: 0x01B4 [0x1D] PRINT_EVENT_MESSAGE(message_id=10205*)
    → "Hah-hah! I get it! You want to be a chef, and hearrrd that Tonberry knives are the best in Vana'diel, rrright?"
  6: 0x01B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01B8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x08)
  8: 0x01BF [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C0   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 29 08 29 A0 0F 01 0B 1D  0B 80 23 29 08 29 A0 0F  ).).......#).)..
01D0: 01 0C 29 08 29 A0 0F 01  0D 1D 0C 80 23 29 08 29  ..).).......#).)
01E0: A0 0F 01 0E 00                                    .....           
```

#### Opcodes

```
  0: 0x01C0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x0B)
  1: 0x01C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=10206*)
    → "But there's no way even the finest chef could use one of those. They're way too dangerrrous!"
  2: 0x01CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x01CB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x0C)
  4: 0x01D2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x0D)
  5: 0x01D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=10207*)
    → "But if you still want one anyway, you're going to have to go to the Temple of Uggalepih. They say that there's a kitchen there where an evil chef spends his days and nights sharrrpening his knives."
  6: 0x01DC [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01DD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x0E)
  8: 0x01E4 [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E5   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                1E F0 FF  FF 7F 6F 70 29 08 29 A0       .....op).).
01F0: 0F 01 0F 1D 0D 80 23 29  08 29 A0 0F 01 10 29 08  ......#).)....).
0200: 29 A0 0F 01 11 1D 0E 80  23 29 08 29 A0 0F 01 12  ).......#).)....
0210: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x01E5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01EA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x01EB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x01EC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x0F)
  4: 0x01F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=10208*)
    → "If you still want a Tonberry knife, you're going to have to go to the Temple of Uggalepih."
  5: 0x01F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01F7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x10)
  7: 0x01FE [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x11)
  8: 0x0205 [0x1D] PRINT_EVENT_MESSAGE(message_id=10209*)
    → "You'll find plenty of knives in the kitchen, but keep a "sharrrp" lookout for the chef! Nya-ha-ha!"
  9: 0x0208 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0209 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x12)
 11: 0x0210 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0212 [0x21] END_EVENT
 13: 0x0213 [0x00] END_REQSTACK()
```

### Event 132

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0214   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:             1E F0 FF FF  7F 6F 70 29 08 29 A0 0F      .....op).)..
0220: 01 01 1D 0F 80 23 29 08  29 A0 0F 01 02 29 08 29  .....#).)....).)
0230: A0 0F 01 09 1D 10 80 23  29 08 29 A0 0F 01 0A 20  .......#).).... 
0240: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0214 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0219 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x021A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x021B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x01)
  4: 0x0222 [0x1D] PRINT_EVENT_MESSAGE(message_id=10210*)
    → "Wow, you rrreally got one! You're the only person I know who would want to get within twenty feet of one of those."
  5: 0x0225 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0226 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x02)
  7: 0x022D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x09)
  8: 0x0234 [0x1D] PRINT_EVENT_MESSAGE(message_id=10211*)
    → "Hey, you're not going to trrry using that thing, are you?"
  9: 0x0237 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0238 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Vah Keshura (ID: 17801257/0x010FA029), tag_num=0x0A)
 11: 0x023F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0241 [0x21] END_EVENT
 13: 0x0242 [0x00] END_REQSTACK()
```
