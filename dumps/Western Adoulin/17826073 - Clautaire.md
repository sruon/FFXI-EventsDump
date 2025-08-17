# 17826073 - Clautaire

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 644 bytes                 |
| Total Events     | 15                        |
| References Count | 37                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [545](#event-545)        | 0x0001       |     47 |             11 |
| [2](#event-2)            | 0x0030       |      1 |              1 |
| [65535.1](#event-655351) | 0x0031       |     36 |              8 |
| [65535.2](#event-655352) | 0x0055       |      8 |              3 |
| [65535.3](#event-655353) | 0x005D       |     32 |              8 |
| [65535.4](#event-655354) | 0x007D       |     31 |              9 |
| [65535.5](#event-655355) | 0x009C       |     15 |              5 |
| [182](#event-182)        | 0x00AB       |      1 |              1 |
| [78](#event-78)          | 0x00AC       |     74 |             22 |
| [77](#event-77)          | 0x00F6       |     48 |             10 |
| [76](#event-76)          | 0x0126       |     91 |             23 |
| [5218](#event-5218)      | 0x0181       |      7 |              2 |
| [65535.6](#event-655356) | 0x0188       |     17 |              5 |
| [65535.7](#event-655357) | 0x0199       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x004B      |          75 |
|       1 | 0x2697      |        9879 |
|       2 | 0x2698      |        9880 |
|       3 | 0x005A      |          90 |
|       4 | 0x001E      |          30 |
|       5 | 0x0028      |          40 |
|       6 | 0x453B      |       17723 |
|       7 | 0x1EEB      |        7915 |
|       8 | 0x0000      |           0 |
|       9 | 0x009A      |         154 |
|      10 | 0x0001      |           1 |
|      11 | 0x002D      |          45 |
|      12 | 0xFFFE4885  |  4294854789 |
|      13 | 0xFFFFB96E  |  4294949230 |
|      14 | 0x0F9F      |        3999 |
|      15 | 0xFFFF3CB0  |  4294917296 |
|      16 | 0xFFFFB7C4  |  4294948804 |
|      17 | 0xFFFFBE60  |  4294950496 |
|      18 | 0x1FBA      |        8122 |
|      19 | 0x1FBB      |        8123 |
|      20 | 0x1FBC      |        8124 |
|      21 | 0x1FBD      |        8125 |
|      22 | 0x0950      |        2384 |
|      23 | 0x1FBE      |        8126 |
|      24 | 0x1FBF      |        8127 |
|      25 | 0x1FC0      |        8128 |
|      26 | 0x1FC1      |        8129 |
|      27 | 0x1FC2      |        8130 |
|      28 | 0x1FC3      |        8131 |
|      29 | 0x1FC4      |        8132 |
|      30 | 0x1FC5      |        8133 |
|      31 | 0x1FC6      |        8134 |
|      32 | 0x00C9      |         201 |
|      33 | 0x6F54      |       28500 |
|      34 | 0xFFFFAAD8  |  4294945496 |
|      35 | 0x03E8      |        1000 |
|      36 | 0x087F      |        2175 |

## String References

- **8122**: Excuse me, [mister/ma'am]--is that a Fantastic Adoulin Imperial Liberators badge I see?
- **8123**: I'm Clautaire! I just joined the Liberators a couple days ago!
- **8124**: I wanna be a pioneer just like you someday, but my parents say I have to go to school first to learn more about the world.
- **8125**: For one of my class projects I'm studying about Adoulin's soil quality. Sounds fun, doesn't it?
- **8126**: But it's not easy. I need $6, but I can't get hold of one myself...
- **8127**: But if you're a pioneer, it must be really easy for you, right? I'd be super happy if you could get one for me.
- **8128**: All I need is $6. Please?
- **8129**: You've brought me the $3! Great!
- **8130**: You pioneers are great! Now I'll ace my project for sure!
- **8131**: I go to a school established by the Order of Renaye and run by the minister of education. Because it's run by the city, it's free to everyone!
- **8132**: There are many poor families like mine, so I think it's great that we're able to study at such a wonderful place!
- **8133**: When I grow up and become a pioneer, I'll be able to help my mother live a better life.
- **8134**: I can't offer you too much, but maybe you'll find this useful? Either way, thank you so much for helping me!
- **9879**: My mother says that pioneers must have brains as well as brawn.
- **9880**: I wish to study hard and become a great pioneer soon! Then maybe I can let her take a break from working so often.

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

### Event 545

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8   .....op[.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 5B  ...tlk0...#...#[
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  ..........tlk1!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9879*)
    → "My mother says that pioneers must have brains as well as brawn."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9880*)
    → "I wish to study hard and become a great pioneer soon! Then maybe I can let her take a break from working so often."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=75*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0030  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 36 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    1C 03 80 5B 00 80 19  01 10 01 19 01 10 01 74   ...[..........t
0040: 6C 6B 31 1C 04 80 32 05  80 1F 00 06 80 07 80 08  lk1...2.........
0050: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0031 [0x1C] WAIT(90* ticks)
  1: 0x0034 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Clautaire (ID: 17826073/0x01100119), Clautaire (ID: 17826073/0x01100119)], work=75*
  2: 0x0043 [0x1C] WAIT(30* ticks)
  3: 0x0046 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  4: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.723*, Z=7.915*, Y=0.000*
  5: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                B6 00 09  80 C0 0A 80 00                ........   
```

#### Opcodes

```
  0: 0x0055 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=154*)
  1: 0x0059 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         1C 0B 80               ...
0060: 32 05 80 1F 00 0C 80 0D  80 0E 80 1F 01 6F 4A F8  2............oJ.
0070: FF FF 7F F0 FF FF 7F 7B  F8 FF FF 7F 00           .......{.....   
```

#### Opcodes

```
  0: 0x005D [0x1C] WAIT(45* ticks)
  1: 0x0060 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=-112.507*, Z=-18.066*, Y=3.999*
  3: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x006D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x006E [0x4A] EventEntity looks at LocalPlayer
  6: 0x0077 [0x7B] EventEntity stops talking
  7: 0x007C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         1C 00 80               ...
0080: 4B 19 01 10 01 08 80 6F  76 19 01 10 01 32 05 80  K......ov....2..
0090: 1F 00 0F 80 10 80 0E 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x007D [0x1C] WAIT(75* ticks)
  1: 0x0080 [0x4B] UPDATE_ENTITY_YAW(entity=Clautaire (ID: 17826073/0x01100119), yaw=0.0°*)
  2: 0x0087 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0088 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Clautaire (ID: 17826073/0x01100119) Render.Flags0 and Render.Flags3 conditions are met
  4: 0x008D [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x0090 [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.000*, Z=-18.492*, Y=3.999*
  6: 0x0098 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x009A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      32 05 80 1F              2...
00A0: 00 0F 80 11 80 0E 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x009C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x009F [0x1F] MOVE_ENTITY: EventEntity moves to X=-50.000*, Z=-16.800*, Y=3.999*
  2: 0x00A7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AA [0x00] END_REQSTACK()
```

### Event 182

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AB  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   00                         .    
```

#### Opcodes

```
  0: 0x00AB [0x00] END_REQSTACK()
```

### Event 78

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 74 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      42 1E F0 FF              B...
00B0: FF 7F 6F 70 5B 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..op[..........t
00C0: 6C 6B 30 1D 12 80 23 1D  13 80 23 1D 14 80 23 1D  lk0...#...#...#.
00D0: 15 80 23 03 02 10 16 80  1D 17 80 23 1D 18 80 23  ..#........#...#
00E0: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 03  [..........tlk1.
00F0: 01 10 0A 80 21 00                                 ....!.          
```

#### Opcodes

```
  0: 0x00AC [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00AD [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00B2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00B3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00B4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  5: 0x00C3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8122*)
    → "Excuse me, [mister/ma'am]--is that a Fantastic Adoulin Imperial Liberators badge I see?"
  6: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8123*)
    → "I'm Clautaire! I just joined the Liberators a couple days ago!"
  8: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00CB [0x1D] PRINT_EVENT_MESSAGE(message_id=8124*)
    → "I wanna be a pioneer just like you someday, but my parents say I have to go to school first to learn more about the world."
 10: 0x00CE [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x00CF [0x1D] PRINT_EVENT_MESSAGE(message_id=8125*)
    → "For one of my class projects I'm studying about Adoulin's soil quality. Sounds fun, doesn't it?"
 12: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x00D3 [0x03] Work_Zone[2] = 2384*
 14: 0x00D8 [0x1D] PRINT_EVENT_MESSAGE(message_id=8126*)
    → "But it's not easy. I need $6, but I can't get hold of one myself..."
 15: 0x00DB [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=8127*)
    → "But if you're a pioneer, it must be really easy for you, right? I'd be super happy if you could get one for me."
 17: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x00E0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=75*
 19: 0x00EF [0x03] Work_Zone[1] = 1*
 20: 0x00F4 [0x21] END_EVENT
 21: 0x00F5 [0x00] END_REQSTACK()
```

### Event 77

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F6   |
| Data Size    | 48 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                   1E F0  FF FF 7F 6F 70 5B 00 80        .....op[..
0100: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 03 02 10 16  ........tlk0....
0110: 80 1D 19 80 23 5B 00 80  F8 FF FF 7F F8 FF FF 7F  ....#[..........
0120: 74 6C 6B 31 21 00                                 tlk1!.          
```

#### Opcodes

```
  0: 0x00F6 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00FB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00FC [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00FD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  4: 0x010C [0x03] Work_Zone[2] = 2384*
  5: 0x0111 [0x1D] PRINT_EVENT_MESSAGE(message_id=8128*)
    → "All I need is $6. Please?"
  6: 0x0114 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0115 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=75*
  8: 0x0124 [0x21] END_EVENT
  9: 0x0125 [0x00] END_REQSTACK()
```

### Event 76

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0126   |
| Data Size    | 91 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                   42 1E  F0 FF FF 7F 6F 70 5B 00        B.....op[.
0130: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 03 02 10  .........tlk0...
0140: 16 80 1D 1A 80 23 1D 1B  80 23 1D 1C 80 23 1D 1D  .....#...#...#..
0150: 80 23 1D 1E 80 23 5B 00  80 F8 FF FF 7F F8 FF FF  .#...#[.........
0160: 7F 70 61 73 30 1D 1F 80  23 45 20 80 F8 FF FF 7F  .pas0...#E .....
0170: F8 FF FF 7F 71 73 74 63  08 80 03 01 10 0A 80 21  ....qstc.......!
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x0126 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0127 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x012C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x012D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x012E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  5: 0x013D [0x03] Work_Zone[2] = 2384*
  6: 0x0142 [0x1D] PRINT_EVENT_MESSAGE(message_id=8129*)
    → "You've brought me the $3! Great!"
  7: 0x0145 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0146 [0x1D] PRINT_EVENT_MESSAGE(message_id=8130*)
    → "You pioneers are great! Now I'll ace my project for sure!"
  9: 0x0149 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x014A [0x1D] PRINT_EVENT_MESSAGE(message_id=8131*)
    → "I go to a school established by the Order of Renaye and run by the minister of education. Because it's run by the city, it's free to everyone!"
 11: 0x014D [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x014E [0x1D] PRINT_EVENT_MESSAGE(message_id=8132*)
    → "There are many poor families like mine, so I think it's great that we're able to study at such a wonderful place!"
 13: 0x0151 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0152 [0x1D] PRINT_EVENT_MESSAGE(message_id=8133*)
    → "When I grow up and become a pioneer, I'll be able to help my mother live a better life."
 15: 0x0155 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0156 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=75*
 17: 0x0165 [0x1D] PRINT_EVENT_MESSAGE(message_id=8134*)
    → "I can't offer you too much, but maybe you'll find this useful? Either way, thank you so much for helping me!"
 18: 0x0168 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0169 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 20: 0x017A [0x03] Work_Zone[1] = 1*
 21: 0x017F [0x21] END_EVENT
 22: 0x0180 [0x00] END_REQSTACK()
```

### Event 5218

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0181  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0181 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0187 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0188   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                          32 05 80 1F 00 21 80 22          2....!."
0190: 80 23 80 1F 01 39 24 80  00                       .#...9$..       
```

#### Opcodes

```
  0: 0x0188 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x018B [0x1F] MOVE_ENTITY: EventEntity moves to X=28.500*, Z=-21.800*, Y=1.000*
  2: 0x0193 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0195 [0x39] SET_ENTITY_DIRECTION(direction=11.9°*)
  4: 0x0198 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0199  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                             7B F8 FF FF 7F 39 24           {....9$
01A0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0199 [0x7B] EventEntity stops talking
  1: 0x019E [0x39] SET_ENTITY_DIRECTION(direction=11.9°*)
  2: 0x01A1 [0x00] END_REQSTACK()
```
