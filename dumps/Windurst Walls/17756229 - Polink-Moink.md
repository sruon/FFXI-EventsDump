# 17756229 - Polink-Moink

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 200 bytes                |
| Total Events     | 7                        |
| References Count | 10                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [302](#event-302)        | 0x0021       |     39 |             13 |
| [11](#event-11)          | 0x0048       |     10 |              2 |
| [206](#event-206)        | 0x0052       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1EE0      |        7904 |
|       3 | 0x1EE1      |        7905 |
|       4 | 0x0375      |         885 |
|       5 | 0xFFFFFB0D  |  4294966029 |
|       6 | 0xFFFFDC2C  |  4294958124 |
|       7 | 0x0E7E      |        3710 |
|       8 | 0x1D83      |        7555 |
|       9 | 0x1D84      |        7556 |

## String References

- **7555**: Oh, you know about those falling stars as well, huh?I've been fortunate enough to eye-spy and peek-a-boo a few of them myself, too.
- **7556**: What did I wish for? Naturally, I wished that Windurst would have everlasting peace and prosperity, joy and security, success and serenity!
- **7904**: That place called Giddeus where all them Yagudo beastmen live and dwell is downright dangerous! If you take one wrong step, then it's bishy-bashy, cracky-whacky, and crunchy-munchy!
- **7905**: Come on! The beastmen have been fighting and slighting with Windurst for hundreds of years! How can anyone expect them to suddenly become all cute-and-cuddly or lovey-dovey?

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                92 01 F8 FF FF 7F            ......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 302

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    86 00 F8 FF FF 7F 1E  F0 FF FF 7F 6F 70 29 0B   ...........op).
0030: 45 F0 0E 01 01 1D 02 80  23 1D 03 80 23 29 0B 45  E.......#...#).E
0040: F0 0E 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0021 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x002E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polink-Moink (ID: 17756229/0x010EF045), tag_num=0x01)
  5: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7904*)
    → "That place called Giddeus where all them Yagudo beastmen live and dwell is downright dangerous! If you take one wrong step, then it's bishy-bashy, cracky-whacky, and crunchy-munchy!"
  6: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7905*)
    → "Come on! The beastmen have been fighting and slighting with Windurst for hundreds of years! How can anyone expect them to suddenly become all cute-and-cuddly or lovey-dovey?"
  8: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polink-Moink (ID: 17756229/0x010EF045), tag_num=0x02)
 10: 0x0044 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0046 [0x21] END_EVENT
 12: 0x0047 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          37 04 80 05 80 06 80 07          7.......
0050: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0048 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.885*, z=-1.267*, y=-9.172*, direction=326.1°*
  1: 0x0051 [0x00] END_REQSTACK()
```

### Event 206

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       1E F0 FF FF 7F 6F  70 29 0B 45 F0 0E 01 01    .....op).E....
0060: 1D 08 80 23 1D 09 80 23  29 0B 45 F0 0E 01 02 20  ...#...#).E.... 
0070: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0052 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0057 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0058 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0059 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polink-Moink (ID: 17756229/0x010EF045), tag_num=0x01)
  4: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=7555*)
    → "Oh, you know about those falling stars as well, huh?I've been fortunate enough to eye-spy and peek-a-boo a few of them myself, too."
  5: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=7556*)
    → "What did I wish for? Naturally, I wished that Windurst would have everlasting peace and prosperity, joy and security, success and serenity!"
  7: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0068 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Polink-Moink (ID: 17756229/0x010EF045), tag_num=0x02)
  9: 0x006F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0071 [0x21] END_EVENT
 11: 0x0072 [0x00] END_REQSTACK()
```
