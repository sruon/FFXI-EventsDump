# 17727571 - Maunadolace

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 88 bytes                  |
| Total Events     | 4                         |
| References Count | 3                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [713](#event-713)        | 0x0001       |     36 |             10 |
| [714](#event-714)        | 0x0025       |      1 |              1 |
| [65535.1](#event-655351) | 0x0026       |      6 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x1EE3      |        7907 |
|       2 | 0x001E      |          30 |

## String References

- **7907**: I am Maunadolace of the Temple Knights, on orders from the prince to watch the auction house. I would love to chat, but I'm on duty.

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

### Event 713

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 5E 69 64 6C 30  ...tlk0...#^idl0
0020: 1C 02 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7907*)
    → "I am Maunadolace of the Temple Knights, on orders from the prince to watch the auction house. I would love to chat, but I'm on duty."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0020 [0x1C] WAIT(30* ticks)
  8: 0x0023 [0x21] END_EVENT
  9: 0x0024 [0x00] END_REQSTACK()
```

### Event 714

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0025  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                00                                      .          
```

#### Opcodes

```
  0: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   5E 69  64 6C 30 00                    ^idl0.    
```

#### Opcodes

```
  0: 0x0026 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002B [0x00] END_REQSTACK()
```
