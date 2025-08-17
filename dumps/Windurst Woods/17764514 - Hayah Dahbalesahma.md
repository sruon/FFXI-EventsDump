# 17764514 - Hayah Dahbalesahma

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 160 bytes                |
| Total Events     | 6                        |
| References Count | 4                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [65535.3](#event-655353) | 0x001A       |     16 |              2 |
| [65535.4](#event-655354) | 0x002A       |     14 |              2 |
| [263](#event-263)        | 0x0038       |     47 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0166      |         358 |
|       1 | 0x001E      |          30 |
|       2 | 0x1F5B      |        8027 |
|       3 | 0x1F5C      |        8028 |

## String References

- **8027**: Would you shut this little cub up for me? She is too pesky and noisy forrr her own good!
- **8028**: The Sibyl Guards are not real Mithra because they werrre raised by Tarutaru! I don't carrre how strong they are. They've lost the Mithra spirrrit.

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                5B 00 80 F8 FF FF            [.....
0020: 7F F8 FF FF 7F 73 69 73  30 00                    .....sis0.      
```

#### Opcodes

```
  0: 0x001A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sis0" with entities [EventEntity, EventEntity], work=358*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                53 F8 FF FF 7F F8            S.....
0030: FF FF 7F 73 69 73 30 00                           ...sis0.        
```

#### Opcodes

```
  0: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sis0" with entities [EventEntity, EventEntity]
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 263

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          1E F0 FF FF 7F 6F 70 29          .....op)
0040: 08 A2 10 0F 01 03 1D 02  80 23 29 08 A2 10 0F 01  .........#).....
0050: 04 29 08 A2 10 0F 01 01  1D 03 80 23 29 08 A2 10  .).........#)...
0060: 0F 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0038 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hayah Dahbalesahma (ID: 17764514/0x010F10A2), tag_num=0x03)
  4: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=8027*)
    → "Would you shut this little cub up for me? She is too pesky and noisy forrr her own good!"
  5: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hayah Dahbalesahma (ID: 17764514/0x010F10A2), tag_num=0x04)
  7: 0x0051 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hayah Dahbalesahma (ID: 17764514/0x010F10A2), tag_num=0x01)
  8: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=8028*)
    → "The Sibyl Guards are not real Mithra because they werrre raised by Tarutaru! I don't carrre how strong they are. They've lost the Mithra spirrrit."
  9: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x005C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hayah Dahbalesahma (ID: 17764514/0x010F10A2), tag_num=0x02)
 11: 0x0063 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0065 [0x21] END_EVENT
 13: 0x0066 [0x00] END_REQSTACK()
```
