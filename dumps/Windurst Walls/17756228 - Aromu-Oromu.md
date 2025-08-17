# 17756228 - Aromu-Oromu

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 124 bytes                |
| Total Events     | 6                        |
| References Count | 4                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [65535.3](#event-655353) | 0x0021       |      1 |              1 |
| [300](#event-300)        | 0x0022       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1EDC      |        7900 |
|       3 | 0x1EDD      |        7901 |

## String References

- **7900**: Our Federation of Windurst is governed-woverned by the great Star Sibyl and the five ministries of magic.
- **7901**: Major decisions are made by the five ministers who head the ministries, but the divinations of the Star Sibyl are the most important determinant.

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0021  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    00                                              .              
```

#### Opcodes

```
  0: 0x0021 [0x00] END_REQSTACK()
```

### Event 300

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       1E F0 FF FF 7F 6F  70 29 0B 44 F0 0E 01 01    .....op).D....
0030: 1D 02 80 23 1D 03 80 23  29 0B 44 F0 0E 01 02 20  ...#...#).D.... 
0040: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0022 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0028 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0029 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Aromu-Oromu (ID: 17756228/0x010EF044), tag_num=0x01)
  4: 0x0030 [0x1D] PRINT_EVENT_MESSAGE(message_id=7900*)
    → "Our Federation of Windurst is governed-woverned by the great Star Sibyl and the five ministries of magic."
  5: 0x0033 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=7901*)
    → "Major decisions are made by the five ministers who head the ministries, but the divinations of the Star Sibyl are the most important determinant."
  7: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0038 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Aromu-Oromu (ID: 17756228/0x010EF044), tag_num=0x02)
  9: 0x003F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0041 [0x21] END_EVENT
 11: 0x0042 [0x00] END_REQSTACK()
```
