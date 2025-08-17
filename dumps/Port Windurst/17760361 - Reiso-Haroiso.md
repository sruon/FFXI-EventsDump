# 17760361 - Reiso-Haroiso

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 116 bytes               |
| Total Events     | 4                       |
| References Count | 4                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [334](#event-334)        | 0x001A       |     39 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0FF5      |        4085 |
|       3 | 0x0FF6      |        4086 |

## String References

- **4085**: I'm glad beastmen don't know how to steer-a-weer ships. You see, Windurst is practically defenseless against attack-a-wacks from the sea.
- **4086**: It'd be a different matter if Cardians could swim-a-wim, but those automatons have a hard enough time trying to keep afloat-a-woat!

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

### Event 334

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                86 00 F8 FF FF 7F            ......
0020: 1E F0 FF FF 7F 6F 70 29  08 69 00 0F 01 01 1D 02  .....op).i......
0030: 80 23 1D 03 80 23 29 08  69 00 0F 01 02 20 00 21  .#...#).i.... .!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0020 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0026 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0027 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Reiso-Haroiso (ID: 17760361/0x010F0069), tag_num=0x01)
  5: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=4085*)
    → "I'm glad beastmen don't know how to steer-a-weer ships. You see, Windurst is practically defenseless against attack-a-wacks from the sea."
  6: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=4086*)
    → "It'd be a different matter if Cardians could swim-a-wim, but those automatons have a hard enough time trying to keep afloat-a-woat!"
  8: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0036 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Reiso-Haroiso (ID: 17760361/0x010F0069), tag_num=0x02)
 10: 0x003D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x003F [0x21] END_EVENT
 12: 0x0040 [0x00] END_REQSTACK()
```
