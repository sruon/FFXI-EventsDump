# 17801231 - Bhi Telifahgo

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 160 bytes        |
| Total Events     | 5                |
| References Count | 5                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [93](#event-93)          | 0x0027       |     33 |             12 |
| [183](#event-183)        | 0x0048       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x2730      |       10032 |
|       3 | 0x2731      |       10033 |
|       4 | 0x287F      |       10367 |

## String References

- **10032**: Whenever I hearrr the sound of the ocean, I always think it sounds like someone calling "slee\`p, slee\`p." Can you hearrr it too, [misterrr/lady]?
- **10033**: You shouldn't fight it when you do. It's best to just lie down and...<yawn>...
- **10367**: Okay, okay! I'm awake. I didn't think anything would wake me up, but that smell sure did the trrrick.

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

### Event 93

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
0030: 0F A0 0F 01 01 1D 02 80  23 1D 03 80 23 29 08 0F  ........#...#)..
0040: A0 0F 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhi Telifahgo (ID: 17801231/0x010FA00F), tag_num=0x01)
  4: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=10032*)
    → "Whenever I hearrr the sound of the ocean, I always think it sounds like someone calling "slee`p, slee`p." Can you hearrr it too, [misterrr/lady]?"
  5: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=10033*)
    → "You shouldn't fight it when you do. It's best to just lie down and...<yawn>..."
  7: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x003D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhi Telifahgo (ID: 17801231/0x010FA00F), tag_num=0x02)
  9: 0x0044 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0046 [0x21] END_EVENT
 11: 0x0047 [0x00] END_REQSTACK()
```

### Event 183

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1E F0 FF FF 7F 6F 70 29          .....op)
0050: 08 0F A0 0F 01 01 1D 04  80 23 29 08 0F A0 0F 01  .........#).....
0060: 02 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0048 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhi Telifahgo (ID: 17801231/0x010FA00F), tag_num=0x01)
  4: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=10367*)
    → "Okay, okay! I'm awake. I didn't think anything would wake me up, but that smell sure did the trrrick."
  5: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Bhi Telifahgo (ID: 17801231/0x010FA00F), tag_num=0x02)
  7: 0x0061 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0063 [0x21] END_EVENT
  9: 0x0064 [0x00] END_REQSTACK()
```
