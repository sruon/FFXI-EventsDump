# 17756253 - Haah Chakaila

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 188 bytes                |
| Total Events     | 7                        |
| References Count | 12                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [65535.3](#event-655353) | 0x0021       |     10 |              2 |
| [65535.4](#event-655354) | 0x002B       |     14 |              4 |
| [330](#event-330)        | 0x0039       |     39 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0166      |         358 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFF6F88  |  4294930312 |
|       3 | 0x214D3     |      136403 |
|       4 | 0xFFFFC180  |  4294951296 |
|       5 | 0x0222      |         546 |
|       6 | 0x000D      |          13 |
|       7 | 0xFFFEDD57  |  4294892887 |
|       8 | 0x1B9D3     |      113107 |
|       9 | 0xFFFFD8F0  |  4294957296 |
|      10 | 0x1F12      |        7954 |
|      11 | 0x1F13      |        7955 |

## String References

- **7954**: Twenty yearrrs ago, the allied forrrces succeeded in defeating the lord of the beastmen. Howeverrr, they were not able to take the beastman forces out completely.
- **7955**: If Windurst had only a little more powerrr then, we could have taken care of our birrrd problem, and there would be no need to fake a happy coexistence with the Yagudo.

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    37 02 80 03 80 04 80  05 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-36.984*, z=136.403*, y=-16.000*, direction=48.0°*
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 06 80 5A 00             2..Z.
0030: 07 80 08 80 09 80 5A 01  00                       ......Z..       
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x002E [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-74.409*, Z=113.107*, Y=-10.000*
  2: 0x0036 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0038 [0x00] END_REQSTACK()
```

### Event 330

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             86 00 F8 FF FF 7F 1E           .......
0040: F0 FF FF 7F 6F 70 29 0B  5D F0 0E 01 01 1D 0A 80  ....op).].......
0050: 23 1D 0B 80 23 29 0B 5D  F0 0E 01 02 20 00 21 00  #...#).].... .!.
```

#### Opcodes

```
  0: 0x0039 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0044 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0045 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0046 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Haah Chakaila (ID: 17756253/0x010EF05D), tag_num=0x01)
  5: 0x004D [0x1D] PRINT_EVENT_MESSAGE(message_id=7954*)
    → "Twenty yearrrs ago, the allied forrrces succeeded in defeating the lord of the beastmen. Howeverrr, they were not able to take the beastman forces out completely."
  6: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0051 [0x1D] PRINT_EVENT_MESSAGE(message_id=7955*)
    → "If Windurst had only a little more powerrr then, we could have taken care of our birrrd problem, and there would be no need to fake a happy coexistence with the Yagudo."
  8: 0x0054 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0055 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Haah Chakaila (ID: 17756253/0x010EF05D), tag_num=0x02)
 10: 0x005C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x005E [0x21] END_EVENT
 12: 0x005F [0x00] END_REQSTACK()
```
