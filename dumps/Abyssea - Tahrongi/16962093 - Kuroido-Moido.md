# 16962093 - Kuroido-Moido

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 72 bytes                    |
| Total Events     | 2                           |
| References Count | 3                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [402](#event-402)     | 0x0001       |     32 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0031      |          49 |
|       1 | 0x1FA6      |        8102 |
|       2 | 0x1FA7      |        8103 |

## String References

- **8102**: Just a ways ahead of here, you'll find a fiery-wiery defensive barrier that we call a searing ward. It keeps us here safe from the dangers that lurk beyond.
- **8103**: Before striking out into the canyon, you should talk to our conflux surveyor and have yourself endowed with visitantaru status. Trust me, you won't want to leave home without it!

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

### Event 402

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 32 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 21  ...tlk0...#...#!
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=8102*)
    → "Just a ways ahead of here, you'll find a fiery-wiery defensive barrier that we call a searing ward. It keeps us here safe from the dangers that lurk beyond."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=8103*)
    → "Before striking out into the canyon, you should talk to our conflux surveyor and have yourself endowed with visitantaru status. Trust me, you won't want to leave home without it!"
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x21] END_EVENT
  9: 0x0020 [0x00] END_REQSTACK()
```
