# 17756246 - Pantsa-Karutsa

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 172 bytes                |
| Total Events     | 7                        |
| References Count | 10                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [65535.3](#event-655353) | 0x0021       |     10 |              2 |
| [65535.4](#event-655354) | 0x002B       |     14 |              4 |
| [301](#event-301)        | 0x0039       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFE8C5C  |  4294872156 |
|       3 | 0x1F236     |      127542 |
|       4 | 0xFFFFEC64  |  4294962276 |
|       5 | 0x00AE      |         174 |
|       6 | 0xFFFE9CCD  |  4294876365 |
|       7 | 0x1E6FA     |      124666 |
|       8 | 0xFFFFEAB0  |  4294961840 |
|       9 | 0x1EDE      |        7902 |

## String References

- **7902**: It was a courageous decision by the Star Sibyl when she set out to make friends with the beastmen. It was because of her actions that we are now able to restore Windurst to the beautaruful place it once was.

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
  0: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-95.140*, z=127.542*, y=-5.020*, direction=15.3°*
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
0020:                                   32 00 80 1F 00             2....
0030: 06 80 07 80 08 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.931*, Z=124.666*, Y=-5.456*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x00] END_REQSTACK()
```

### Event 301

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             1E F0 FF FF 7F 6F 70           .....op
0040: 29 0B 56 F0 0E 01 01 1D  09 80 23 29 0B 56 F0 0E  ).V.......#).V..
0050: 01 02 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0040 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pantsa-Karutsa (ID: 17756246/0x010EF056), tag_num=0x01)
  4: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=7902*)
    → "It was a courageous decision by the Star Sibyl when she set out to make friends with the beastmen. It was because of her actions that we are now able to restore Windurst to the beautaruful place it once was."
  5: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Pantsa-Karutsa (ID: 17756246/0x010EF056), tag_num=0x02)
  7: 0x0052 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0054 [0x21] END_EVENT
  9: 0x0055 [0x00] END_REQSTACK()
```
