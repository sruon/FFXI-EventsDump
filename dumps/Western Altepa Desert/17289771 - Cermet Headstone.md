# 17289771 - Cermet Headstone

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Western Altepa Desert (ID: 125) |
| Block Size       | 80 bytes                        |
| Total Events     | 2                               |
| References Count | 4                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [200](#event-200)     | 0x0001       |     39 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CC2      |        7362 |
|       1 | 0x1CC3      |        7363 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |

## String References

- **7362**: 6... A single fragment of light. The way in which it shines suggests that it is resonating with something...
- **7363**: Do you remove the $3? [Yes./No.]

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

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F F8 FF  FF 7F 48 00 80 23 24 01   J........H..#$.
0010: 80 02 80 02 80 25 02 00  10 02 80 00 26 00 03 01  .....%......&...
0020: 10 03 80 01 26 00 21 00                           ....&.!.        
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at EventEntity
  1: 0x000A [0x48] [System] [7362*]:
    → "6... A single fragment of light. The way in which it shines suggests that it is resonating with something..."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x24] CREATE_DIALOG(message_id=7363*, default_option=0*, option_flags=0*)
    → "Do you remove the $3? [Yes./No.]"
  4: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0026
  6: 0x001E [0x03] Work_Zone[1] = 1*
  7: 0x0023 [0x01] GOTO 0x0026

SUBROUTINE_0026:
  8: 0x0026 [0x21] END_EVENT
  9: 0x0027 [0x00] END_REQSTACK()
```
