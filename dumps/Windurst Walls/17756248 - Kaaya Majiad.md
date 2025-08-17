# 17756248 - Kaaya Majiad

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 348 bytes                |
| Total Events     | 11                       |
| References Count | 20                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              2 |
| [65535.5](#event-655355) | 0x0045       |      9 |              3 |
| [443](#event-443)        | 0x004E       |     10 |              2 |
| [65535.6](#event-655356) | 0x0058       |     14 |              4 |
| [323](#event-323)        | 0x0066       |     60 |             17 |
| [11](#event-11)          | 0x00A2       |     10 |              2 |
| [208](#event-208)        | 0x00AC       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0166      |         358 |
|       1 | 0x001E      |          30 |
|       2 | 0x016C      |         364 |
|       3 | 0xFFFE939B  |  4294874011 |
|       4 | 0x1FA59     |      129625 |
|       5 | 0xFFFFEBED  |  4294962157 |
|       6 | 0x01DE      |         478 |
|       7 | 0x000D      |          13 |
|       8 | 0xFFFEA33E  |  4294878014 |
|       9 | 0x1F00C     |      126988 |
|      10 | 0xFFFFEB4C  |  4294961996 |
|      11 | 0x0844      |        2116 |
|      12 | 0x1F04      |        7940 |
|      13 | 0x1F05      |        7941 |
|      14 | 0x1EB8      |        7864 |
|      15 | 0xFFFFC74A  |  4294952778 |
|      16 | 0xFFFFDBE5  |  4294958053 |
|      17 | 0x0C6F      |        3183 |
|      18 | 0x1D87      |        7559 |
|      19 | 0x1D88      |        7560 |

## String References

- **7559**: The Tarutaru go all silly over making wishes on falling starrrs, but we Mithra don't believe in such nonsense.
- **7560**: It's probably a harrrbinger that something really bad's about to happen. Heh, and about time, too. I've been yearrrning to run wild for a bit. Ahh, my blood is rrrushing already!
- **7940**: If you need to enter Heavens Tower, then you'll have to crrross that bridge over there. Look around you, and you'll realize that the ruins of the once-grrreat walls of Windurst are prrractically filled with water.
- **7941**: It was twenty years ago, during the Grrreat War, when the walls were destroyed and the place became flooded. But betterrr to have an abundance of waterrr than none at all, eh?

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=358*
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
0020:                      5B  02 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 70 6F 69 30 00                              ..poi0.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=364*
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
0040: 70 6F 69 30 00                                    poi0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                5E 69 64  6C 30 1C 01 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x0045 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x004A [0x1C] WAIT(30* ticks)
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            37 03                7.
0050: 80 04 80 05 80 06 80 00                           ........        
```

#### Opcodes

```
  0: 0x004E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-93.285*, z=129.625*, y=-5.139*, direction=42.0°*
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          32 07 80 1F 00 08 80 09          2.......
0060: 80 0A 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0058 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005B [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.282*, Z=126.988*, Y=-5.300*
  2: 0x0063 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0065 [0x00] END_REQSTACK()
```

### Event 323

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 60 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   4B 58  F0 0E 01 0B 80 6F 76 58        KX.....ovX
0070: F0 0E 01 29 08 58 F0 0E  01 03 1D 0C 80 23 29 08  ...).X.......#).
0080: 58 F0 0E 01 04 1E F0 FF  FF 7F 6F 70 29 08 58 F0  X.........op).X.
0090: 0E 01 01 1D 0D 80 23 29  08 58 F0 0E 01 05 20 00  ......#).X.... .
00A0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0066 [0x4B] UPDATE_ENTITY_YAW(entity=Kaaya Majiad (ID: 17756248/0x010EF058), yaw=11.6°*)
  1: 0x006D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x006E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Kaaya Majiad (ID: 17756248/0x010EF058) Render.Flags0 and Render.Flags3 conditions are met
  3: 0x0073 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kaaya Majiad (ID: 17756248/0x010EF058), tag_num=0x03)
  4: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=7940*)
    → "If you need to enter Heavens Tower, then you'll have to crrross that bridge over there. Look around you, and you'll realize that the ruins of the once-grrreat walls of Windurst are prrractically filled with water."
  5: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kaaya Majiad (ID: 17756248/0x010EF058), tag_num=0x04)
  7: 0x0085 [0x1E] EventEntity looks at LocalPlayer and starts talking
  8: 0x008A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x008B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x008C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kaaya Majiad (ID: 17756248/0x010EF058), tag_num=0x01)
 11: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=7941*)
    → "It was twenty years ago, during the Grrreat War, when the walls were destroyed and the place became flooded. But betterrr to have an abundance of waterrr than none at all, eh?"
 12: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0097 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kaaya Majiad (ID: 17756248/0x010EF058), tag_num=0x05)
 14: 0x009E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 15: 0x00A0 [0x21] END_EVENT
 16: 0x00A1 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A2   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       37 0E 80 0F 80 10  80 11 80 00                7.........    
```

#### Opcodes

```
  0: 0x00A2 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=7.864*, z=-14.518*, y=-9.243*, direction=279.7°*
  1: 0x00AB [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AC   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                      1E F0 FF FF              ....
00B0: 7F 6F 70 29 0B 58 F0 0E  01 01 1D 12 80 23 1D 13  .op).X.......#..
00C0: 80 23 29 0B 58 F0 0E 01  05 20 00 21 00           .#).X.... .!.   
```

#### Opcodes

```
  0: 0x00AC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B3 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kaaya Majiad (ID: 17756248/0x010EF058), tag_num=0x01)
  4: 0x00BA [0x1D] PRINT_EVENT_MESSAGE(message_id=7559*)
    → "The Tarutaru go all silly over making wishes on falling starrrs, but we Mithra don't believe in such nonsense."
  5: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00BE [0x1D] PRINT_EVENT_MESSAGE(message_id=7560*)
    → "It's probably a harrrbinger that something really bad's about to happen. Heh, and about time, too. I've been yearrrning to run wild for a bit. Ahh, my blood is rrrushing already!"
  7: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00C2 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Kaaya Majiad (ID: 17756248/0x010EF058), tag_num=0x05)
  9: 0x00C9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00CB [0x21] END_EVENT
 11: 0x00CC [0x00] END_REQSTACK()
```
