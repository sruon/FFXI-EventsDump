# 17723462 - Pala Korin

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 96 bytes                      |
| Total Events     | 2                             |
| References Count | 5                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [555](#event-555)     | 0x0001       |     50 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x0588      |        1416 |
|       2 | 0x0034      |          52 |
|       3 | 0x2CC4      |       11460 |
|       4 | 0x001E      |          30 |

## String References

- **11460**: Welcome to the Consulate of Windurst. Consul Kasaroro is inside, if you're looking forrr her.

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

### Event 555

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 50 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 39 01 80 6F 70 66 02   ........9..opf.
0010: 80 F8 FF FF 7F F8 FF FF  7F 70 6F 69 30 1D 03 80  .........poi0...
0020: 23 53 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 30 1C 04  #S........poi0..
0030: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(60* ticks)
  2: 0x0009 [0x39] SET_ENTITY_DIRECTION(direction=7.8°*)
  3: 0x000C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x000D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x000E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=52*
  6: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=11460*)
    → "Welcome to the Consulate of Windurst. Consul Kasaroro is inside, if you're looking forrr her."
  7: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0021 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  9: 0x002E [0x1C] WAIT(30* ticks)
 10: 0x0031 [0x21] END_EVENT
 11: 0x0032 [0x00] END_REQSTACK()
```
