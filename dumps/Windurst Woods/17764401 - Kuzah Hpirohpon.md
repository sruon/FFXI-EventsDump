# 17764401 - Kuzah Hpirohpon

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 52 bytes                 |
| Total Events     | 2                        |
| References Count | 2                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [250](#event-250)     | 0x0001       |     19 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F47      |        8007 |
|       1 | 0x1F48      |        8008 |

## String References

- **8007**: Sew...I mean..."So," want to get your paws on the top-quality materials as used in the Weaverrrs' Guild?
- **8008**: Then step rrright up and take a look! Just be carrreful not to get too giddy with excitement, now!

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

### Event 250

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 1D 01 80 23   .....op...#...#
0010: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8007*)
    → "Sew...I mean..."So," want to get your paws on the top-quality materials as used in the Weaverrrs' Guild?"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=8008*)
    → "Then step rrright up and take a look! Just be carrreful not to get too giddy with excitement, now!"
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0012 [0x21] END_EVENT
  9: 0x0013 [0x00] END_REQSTACK()
```
