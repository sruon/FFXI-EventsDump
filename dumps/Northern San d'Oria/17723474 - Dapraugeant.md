# 17723474 - Dapraugeant

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 136 bytes                     |
| Total Events     | 4                             |
| References Count | 10                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [535](#event-535)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     23 |              5 |
| [532](#event-532)        | 0x0019       |     36 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFDE113  |  4294828307 |
|       2 | 0x32A31     |      207409 |
|       3 | 0x2EDF      |       11999 |
|       4 | 0x0CC0      |        3264 |
|       5 | 0xFFFE043B  |  4294837307 |
|       6 | 0x3B164     |      242020 |
|       7 | 0x0014      |          20 |
|       8 | 0x2C18      |       11288 |
|       9 | 0x001E      |          30 |

## String References

- **11288**: This is the entrance to the watchtower, which overlooks the woods of Ronfaure.

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

### Event 535

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
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 37 01 80  02 80 03 80 04 80 1F 00    2..7..........
0010: 05 80 06 80 03 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-138.989*, z=207.409*, y=11.999*, direction=286.9°*
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-129.989*, Z=242.020*, Y=11.999*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 532

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1E F0 FF FF 7F 6F 70           .....op
0020: 66 07 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0030: 08 80 23 5E 69 64 6C 30  1C 09 80 21 00           ..#^idl0...!.   
```

#### Opcodes

```
  0: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x001F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0020 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=11288*)
    → "This is the entrance to the watchtower, which overlooks the woods of Ronfaure."
  5: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0033 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0038 [0x1C] WAIT(30* ticks)
  8: 0x003B [0x21] END_EVENT
  9: 0x003C [0x00] END_REQSTACK()
```
