# 16839271 - Red Canyon

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Konschtat (ID: 15) |
| Block Size       | 100 bytes                    |
| Total Events     | 2                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [291](#event-291)     | 0x0001       |     53 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F78      |        8056 |
|       1 | 0x0000      |           0 |
|       2 | 0x0078      |         120 |
|       3 | 0x0300      |         768 |
|       4 | 0x002F      |          47 |

## String References

- **8056**: On our last field patrol, we came across a conflux to the southeast of here. You'd do well to go imprint with it if you haven't already.

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

### Event 291

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 53 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1A 13 00 1E F0 FF  FF 7F 1D 00 80 23 1A 23   B...........#.#
0010: 00 21 00 86 01 F8 FF FF  7F AB 03 AC 01 01 80 1C  .!..............
0020: 02 80 1B 86 01 F8 FF FF  7F 39 03 80 AC 01 04 80  .........9......
0030: AB 04 1C 02 80 1B                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1A] CALL_SUBROUTINE(address=0x0013)
  2: 0x0005 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8056*)
    → "On our last field patrol, we came across a conflux to the southeast of here. You'd do well to go imprint with it if you haven't already."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1A] CALL_SUBROUTINE(address=0x0023)
  6: 0x0011 [0x21] END_EVENT
  7: 0x0012 [0x00] END_REQSTACK()

SUBROUTINE_0013:
  8: 0x0013 [0x86] EventEntity->Render.Flags3 ^= 0x01
  9: 0x0019 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
 10: 0x001B [0xAC] EventEntity->StatusEvent = 0*
 11: 0x001F [0x1C] WAIT(120* ticks)
 12: 0x0022 [0x1B] RETURN

SUBROUTINE_0023:
 13: 0x0023 [0x86] EventEntity->Render.Flags3 ^= 0x01
 14: 0x0029 [0x39] SET_ENTITY_DIRECTION(direction=4.2°*)
 15: 0x002C [0xAC] EventEntity->StatusEvent = 47*
 16: 0x0030 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
 17: 0x0032 [0x1C] WAIT(120* ticks)
 18: 0x0035 [0x1B] RETURN
```
