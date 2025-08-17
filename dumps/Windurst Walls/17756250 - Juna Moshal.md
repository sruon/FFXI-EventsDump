# 17756250 - Juna Moshal

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 152 bytes                |
| Total Events     | 7                        |
| References Count | 8                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [327](#event-327)        | 0x0021       |     25 |             11 |
| [499](#event-499)        | 0x003A       |      1 |              1 |
| [65535.3](#event-655353) | 0x003B       |     15 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x1F0C      |        7948 |
|       3 | 0x1F0D      |        7949 |
|       4 | 0xFFFFFC42  |  4294966338 |
|       5 | 0x45DF8     |      286200 |
|       6 | 0xFFFFD8F0  |  4294957296 |
|       7 | 0x0C9C      |        3228 |

## String References

- **7948**: <Hiss!> Get out of herrre.
- **7949**: We kids keep our tails out of you adults' business, so you keep your big noses out of ourrrs!

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
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

### Event 327

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 25 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    86 00 F8 FF FF 7F 1E  F0 FF FF 7F 6F 70 1D 02   ...........op..
0030: 80 23 1D 03 80 23 20 00  21 00                    .#...# .!.      
```

#### Opcodes

```
  0: 0x0021 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7948*)
    → "<Hiss!> Get out of herrre."
  5: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=7949*)
    → "We kids keep our tails out of you adults' business, so you keep your big noses out of ourrrs!"
  7: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0036 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0038 [0x21] END_EVENT
 10: 0x0039 [0x00] END_REQSTACK()
```

### Event 499

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                00                           .     
```

#### Opcodes

```
  0: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   37 04 80 05 80             7....
0040: 06 80 07 80 80 F8 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x003B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.958*, z=286.200*, y=-10.000*, direction=283.7°*
  1: 0x0044 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x0049 [0x00] END_REQSTACK()
```
