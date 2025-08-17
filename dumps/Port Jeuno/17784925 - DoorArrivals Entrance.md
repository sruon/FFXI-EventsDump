# 17784925 - DoorArrivals Entrance

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 220 bytes            |
| Total Events     | 2                    |
| References Count | 10                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [52](#event-52)       | 0x0001       |    154 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF1E2B  |  4294909483 |
|       1 | 0x1BB3      |        7091 |
|       2 | 0x1BB4      |        7092 |
|       3 | 0x1BB5      |        7093 |
|       4 | 0x0001      |           1 |
|       5 | 0x0000      |           0 |
|       6 | 0x0092      |         146 |
|       7 | 0x003C      |          60 |
|       8 | 0x00C8      |         200 |
|       9 | 0x001E      |          30 |

## String References

- **7093**: Proceed to the air travel agency? [Yes./No.]

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

### Event 52

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 154 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    3B F0 FF FF 7F 01 00  02 00 03 00 02 02 00 00   ;..............
0010: 80 02 28 00 4A 17 60 0F  01 F0 FF FF 7F 2B 17 60  ..(.J.`......+.`
0020: 0F 01 01 80 23 01 99 00  4A 16 60 0F 01 F0 FF FF  ....#...J.`.....
0030: 7F 2B 16 60 0F 01 02 80  23 24 03 80 04 80 05 80  .+.`....#$......
0040: 25 02 00 10 05 80 00 99  00 42 27 0A F0 FF FF 7F  %........B'.....
0050: 16 46 01 4C 45 06 80 F0  FF FF 7F F0 FF FF 7F 63  .F.LE..........c
0060: 6D 35 33 05 80 2A 0A F0  FF FF 7F 4D 1C 07 80 45  m53..*.....M...E
0070: 08 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 30 05 80  ..........fdo0..
0080: 1C 09 80 46 00 45 08 80  F0 FF FF 7F F0 FF FF 7F  ...F.E..........
0090: 66 64 69 30 05 80 01 99  00 21 00                 fdi0.....!.     
```

#### Opcodes

```
  0: 0x0001 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  1: 0x000C [0x02] IF !(ExtData[1]->WorkLocal[2] <= 4294909483*) GOTO 0x0028
  2: 0x0014 [0x4A] White Beetle (ID: 17784855/0x010F6017) looks at LocalPlayer
  3: 0x001D [0x2B] White Beetle (ID: 17784855/0x010F6017) [7091*]:
    → "This is the arrivals exit. The entrance to departures is next door."
  4: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0025 [0x01] GOTO 0x0099
  6: 0x0028 [0x4A] Nikki (ID: 17784854/0x010F6016) looks at LocalPlayer
  7: 0x0031 [0x2B] Nikki (ID: 17784854/0x010F6016) [7092*]:
    → "Once you go through customs, you'll have to pay to come back on board. Is that all right?"
  8: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0039 [0x24] CREATE_DIALOG(message_id=7093*, default_option=1*, option_flags=0*)
    → "Proceed to the air travel agency? [Yes./No.]"
 10: 0x0040 [0x25] WAIT_DIALOG_SELECT()
 11: 0x0041 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0099
 12: 0x0049 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 13: 0x004A [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x16)
 14: 0x0051 [0x46] CAMERA_CONTROL: Disable user control
 15: 0x0053 [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x0054 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm53" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 17: 0x0065 [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 18: 0x006B [0x4D] EventEntity->StatusEvent = 9 // Close door
 19: 0x006C [0x1C] WAIT(60* ticks)
 20: 0x006F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x0080 [0x1C] WAIT(30* ticks)
 22: 0x0083 [0x46] CAMERA_CONTROL: Restore default settings
 23: 0x0085 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x0096 [0x01] GOTO 0x0099

SUBROUTINE_0099:
 25: 0x0099 [0x21] END_EVENT
 26: 0x009A [0x00] END_REQSTACK()
```
