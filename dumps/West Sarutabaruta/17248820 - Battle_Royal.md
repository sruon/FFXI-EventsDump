# 17248820 - Battle_Royal

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 80 bytes                    |
| Total Events     | 2                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [51](#event-51)       | 0x0001       |     38 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x40000000  |  1073741824 |
|       1 | 0x1E90      |        7824 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |

## String References

- **7824**: Are you ready to take part in the CONFLICT? [I was born ready./I'd rather wash my hair.]

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

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 38 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  03 01 10 00 80 24 01 80   .....op.....$..
0010: 02 80 03 80 25 02 00 10  03 80 00 25 00 03 01 10  ....%......%....
0020: 03 80 01 25 00 21 00                              ...%.!.         
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x03] Work_Zone[1] = 1073741824*
  4: 0x000D [0x24] CREATE_DIALOG(message_id=7824*, default_option=1*, option_flags=0*)
    → "Are you ready to take part in the CONFLICT? [I was born ready./I'd rather wash my hair.]"
  5: 0x0014 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0015 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0025
  7: 0x001D [0x03] Work_Zone[1] = 0*
  8: 0x0022 [0x01] GOTO 0x0025

SUBROUTINE_0025:
  9: 0x0025 [0x21] END_EVENT
 10: 0x0026 [0x00] END_REQSTACK()
```
