# 17801277 - Kyun Magopiteh

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 172 bytes        |
| Total Events     | 7                |
| References Count | 6                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [86](#event-86)          | 0x001A       |     40 |             13 |
| [174](#event-174)        | 0x0042       |     33 |             12 |
| [295](#event-295)        | 0x0063       |      1 |              1 |
| [297](#event-297)        | 0x0064       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x2718      |       10008 |
|       3 | 0x2719      |       10009 |
|       4 | 0x2870      |       10352 |
|       5 | 0x2871      |       10353 |

## String References

- **10008**: You're one of those [people/people/people/people/people/people/people/Mithra/people] borrrn over in the mainlands.
- **10009**: You may think that we Mithra all wanderrr around, never settling down in one place, but you're wrong. Spend a little time here, and you'll see our true colors.
- **10352**: So anotherrr mainlander went off and stuck [his/her] nose where it didn't belong... When will you people learrrn?
- **10353**: Head over to M & P's. I think I rrremember them talking about an ancient method of rrremoving that smell. Not that it's going to work...

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

### Event 86

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 40 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 08 3D A0 0F 01 01  29 08 F0 FF FF 7F 04 1D  p).=....).......
0030: 02 80 23 1D 03 80 23 29  08 3D A0 0F 01 02 20 00  ..#...#).=.... .
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kyun Magopiteh (ID: 17801277/0x010FA03D), tag_num=0x01)
  4: 0x0028 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=LocalPlayer, tag_num=0x04)
  5: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=10008*)
    → "You're one of those [people/people/people/people/people/people/people/Mithra/people] borrrn over in the mainlands."
  6: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=10009*)
    → "You may think that we Mithra all wanderrr around, never settling down in one place, but you're wrong. Spend a little time here, and you'll see our true colors."
  8: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kyun Magopiteh (ID: 17801277/0x010FA03D), tag_num=0x02)
 10: 0x003E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0040 [0x21] END_EVENT
 12: 0x0041 [0x00] END_REQSTACK()
```

### Event 174

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       1E F0 FF FF 7F 6F  70 29 08 3D A0 0F 01 01    .....op).=....
0050: 1D 04 80 23 1D 05 80 23  29 08 3D A0 0F 01 02 20  ...#...#).=.... 
0060: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0048 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0049 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kyun Magopiteh (ID: 17801277/0x010FA03D), tag_num=0x01)
  4: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=10352*)
    → "So anotherrr mainlander went off and stuck [his/her] nose where it didn't belong... When will you people learrrn?"
  5: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=10353*)
    → "Head over to M & P's. I think I rrremember them talking about an ancient method of rrremoving that smell. Not that it's going to work..."
  7: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0058 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Kyun Magopiteh (ID: 17801277/0x010FA03D), tag_num=0x02)
  9: 0x005F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0061 [0x21] END_EVENT
 11: 0x0062 [0x00] END_REQSTACK()
```

### Event 295

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 297

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             00                                        .           
```

#### Opcodes

```
  0: 0x0064 [0x00] END_REQSTACK()
```
